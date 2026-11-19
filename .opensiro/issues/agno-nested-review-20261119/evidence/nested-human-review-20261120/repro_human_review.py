import json
import asyncio
from agno.workflow import Condition, HumanReview, Loop, Parallel, Router, Step, Steps, Workflow

async def run_case(mode, review_type, execution):
    ran=[]
    def draft(step_input): ran.append('draft'); return 'draft text'
    def publish(step_input): ran.append('publish'); return 'published'
    review = HumanReview(**{review_type: True})
    wrapped=lambda s: s
    if mode=='Condition': wrapped=lambda s: Condition(name='c',evaluator=lambda si: True,steps=[s])
    elif mode=='Loop': wrapped=lambda s: Loop(name='l',steps=[s],max_iterations=1)
    elif mode=='Parallel': wrapped=lambda s: Parallel(s,name='p')
    elif mode=='Steps': wrapped=lambda s: Steps(name='s',steps=[s])
    elif mode=='Router': wrapped=lambda s: Router(name='r',choices=[s],selector=lambda si: [s])
    try:
        step=Step(name='draft',executor=draft,human_review=review)
        workflow=Workflow(name=mode,steps=[wrapped(step),Step(name='publish',executor=publish)])
        out=workflow.run(input='go') if execution=='sync' else await workflow.arun(input='go')
        req=getattr(out,'step_requirements',None)
        return {'execution':execution,'mode':mode,'review':review_type,'paused':out.is_paused,'awaiting_output_review':len(out.steps_requiring_output_review or []),'requirements':len(req or []),'ran':ran}
    except Exception as exc:
        return {'execution':execution,'mode':mode,'review':review_type,'error':type(exc).__name__+': '+str(exc),'ran':ran}

modes=['top_level','Condition','Loop','Parallel','Steps','Router']
async def main():
    all_results=[]
    for ex in ('sync','async'):
        for t in ('requires_output_review','requires_confirmation'):
            for m in modes:
                all_results.append(await run_case(m,t,ex))
    # Confirm this source revision still has the reported fail-open behavior.
    assert len(all_results)==24
    assert not any('error' in x for x in all_results)
    parents=[x for x in all_results if x['mode']=='top_level']
    nested=[x for x in all_results if x['mode']!='top_level']
    assert len(parents)==4 and all(x['paused'] for x in parents)
    assert len(nested)==20 and all(
       x['paused'] is False and x['requirements']==0 and x['ran']==['draft','publish']
       for x in nested
    )
    print(json.dumps(all_results,indent=2))
    open('repro_results.json','w').write(json.dumps(all_results,indent=2)+'\n')
if __name__=='__main__':
    asyncio.run(main())
