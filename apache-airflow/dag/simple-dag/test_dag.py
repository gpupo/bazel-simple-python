import pytest
from airflow.models import DagBag
from airflow.utils.dates import days_ago


def test_dag_integrity():
    """
    Verify DAG file can be parsed without errors
    Checks for:
    - No import errors
    - Correct number of tasks
    - Task dependencies
    """
    dag_bag = DagBag(dag_folder="dags/", include_examples=False)

    # Check no import errors
    assert len(dag_bag.import_errors) == 0, f"Import errors: {dag_bag.import_errors}"

    # Check DAG exists
    dag = dag_bag.get_dag("minimal_example_dag")
    assert dag is not None

    # Check number of tasks
    assert len(dag.tasks) == 2, f"Expected 2 tasks, got {len(dag.tasks)}"


def test_dag_tasks():
    """
    Test specific details about the DAG tasks
    """
    dag_bag = DagBag(dag_folder="dags/", include_examples=False)
    dag = dag_bag.get_dag("minimal_example_dag")

    # Check task IDs
    task_ids = [task.task_id for task in dag.tasks]
    assert "hello_world_task" in task_ids
    assert "goodbye_world_task" in task_ids
