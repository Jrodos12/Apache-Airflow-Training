from airflow import DAG
from airflow.sdk import task,dag
from src.hello_world_task_api import print_hello
from datetime import datetime
from datetime import timedelta




default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
@dag('first_dag_with_task_api',
        default_args=default_args,
        schedule='@once',
        catchup=False,
        tags=['workflow_api']
    )
def dag_with_taskflow_api():
    @task
    def task_1():
        print_hello()
    a = task_1()

dag_with_taskflow_api()
