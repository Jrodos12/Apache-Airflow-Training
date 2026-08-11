from airflow import DAG
from airflow.sdk import task,dag
from src.mutiple_task_with_api import task_a,task_b,task_c,task_d,task_e
from datetime import datetime
from datetime import timedelta

default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
@dag('multiple_task_with_api',
        default_args=default_args,
        schedule='@once',
        catchup=False,
        tags=['workflow_api']
    )
def dag_with_taskflow_api():
    @task
    def task1():
        task_a()
    @task
    def task2():
        task_b()
    @task
    def task3():
        task_c()
    @task
    def task4():
        task_d()
    @task
    def task5():
        task_e()
    
    a = task1()
    b = task2()
    c = task3()
    d = task4()
    e = task5()
    a >> [b,c,d] >> e


dag_with_taskflow_api()
