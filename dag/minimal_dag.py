from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def hello_world():
    """Simple function to print a hello world message."""
    print("Hello, Airflow!")


def goodbye_world():
    """Simple function to print a goodbye world message."""
    print("Goodbye, Airflow!")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "minimal_example_dag",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:
    task1 = PythonOperator(
        task_id="hello_world_task",
        python_callable=hello_world,
        dag=dag,
    )

    task2 = PythonOperator(
        task_id="goodbye_world_task",
        python_callable=goodbye_world,
        dag=dag,
    )

    task1 >> task2
