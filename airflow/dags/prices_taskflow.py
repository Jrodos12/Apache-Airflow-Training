from airflow import DAG
from airflow.sdk import task,dag
from src.prices import get_order_price_data,compute_sum,compute_avg,display_result
from datetime import datetime
from datetime import timedelta

default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
@dag('xcom_with_taskflow_api',
        default_args=default_args,
        schedule='@once',
        catchup=False,
        tags=['workflow_api']
    )
def dag_with_taskflow_api():

    @task
    def get_order_price_data_task():
        return get_order_price_data()

    @task
    def compute_sum_task(order_data:dict):
        return compute_sum(order_price_data=order_data)

    @task
    def compute_avg_task(order_data:dict):
        return compute_avg(order_price_data=order_data)

    @task
    def display_result_task(total:float, average:float):
        display_result(total,average)
    
    data = get_order_price_data_task()
    total = compute_sum_task(data)
    average = compute_avg_task(data)
    result = display_result_task(total,average)
    data >> [total,average] >> result


dag_with_taskflow_api()
