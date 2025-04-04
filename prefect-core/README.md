Exemplo de uso da lib `packages/snakesay` de outro `uv workspace` em `prefect-core/flows/snakesay_flow.py`.

As inclusoes necessarias em pyproject.toml sao obtidas por `uv add snakesay`.

    uv run prefect-core/flows/snakesay_flow.py

Output

```
08:31:37.306 | INFO    | prefect.engine - Created flow run 'spectacular-owl' for flow 'say-flow'
08:31:37.384 | INFO    | Flow run 'spectacular-owl' - Created task run 'say_task-0' for task 'say_task'
08:31:37.384 | INFO    | Flow run 'spectacular-owl' - Executing 'say_task-0' immediately...
08:31:37.430 | INFO    | Task run 'say_task-0' -  __________________________
08:31:37.431 | INFO    | Task run 'say_task-0' - ( Hello from Prefect Flow! )
08:31:37.431 | INFO    | Task run 'say_task-0' -  __________________________
08:31:37.432 | INFO    | Task run 'say_task-0' -   \
08:31:37.434 | INFO    | Task run 'say_task-0' -    \    ___
08:31:37.434 | INFO    | Task run 'say_task-0' -     \  (o o)
08:31:37.435 | INFO    | Task run 'say_task-0' -         \_/ \
08:31:37.435 | INFO    | Task run 'say_task-0' -          λ \ \
08:31:37.436 | INFO    | Task run 'say_task-0' -            _\ \_
08:31:37.436 | INFO    | Task run 'say_task-0' -           (_____)_
08:31:37.437 | INFO    | Task run 'say_task-0' -          (________)=Oo°
08:31:37.472 | INFO    | Task run 'say_task-0' - Finished in state Completed()
08:31:37.474 | INFO    | Flow run 'spectacular-owl' - None
08:31:37.501 | INFO    | Flow run 'spectacular-owl' - Finished in state Completed('All states completed.')

```
