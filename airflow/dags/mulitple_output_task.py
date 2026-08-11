from airflow import DAG
from airflow.sdk import task,dag
from src.prices_multy_return import get_order_price_data,compute_sum_and_average,display_result
from datetime import datetime
from datetime import timedelta

default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
@dag('multiple_output_xcomm',
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
    def compute_sum_and_average_task(order_data:dict):
        return compute_sum_and_average(order_price_data=order_data)


    @task
    def display_result_task(summary_data):
        display_result(summary_data)
    
    data = get_order_price_data_task()
    summary_data = compute_sum_and_average_task(data)
    result = display_result_task(summary_data)


dag_with_taskflow_api()
