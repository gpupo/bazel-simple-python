import os
import sys
from datetime import datetime

# Add Airflow to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the DAG
from minimal_dag import dag


def local_run():
    """
    Run the DAG locally for testing and development
    """
    # Get the DAG object
    print("Running DAG locally...")

    # Run each task sequentially
    for task in dag.tasks:
        print(f"Executing task: {task.task_id}")
        try:
            task.execute(
                context={"dag": dag, "task": task, "execution_date": datetime.now()}
            )
        except Exception as e:
            print(f"Error executing {task.task_id}: {e}")
            raise


if __name__ == "__main__":
    local_run()
