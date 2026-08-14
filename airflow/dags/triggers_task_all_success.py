from airflow.sdk import  task,dag,TriggerRule
from datetime import datetime,timedelta
from src.triggers import *
default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

@dag('trigger_task',
    schedule='@once',
    catchup=False,
    tags=['workflow_api','trigger','decorators'],
    default_args=default_args
)
def triggers_pipeline():
    @task(task_id="start")
    def start():
        succeed()
    
    @task(task_id="Payment_succeed")
    def payment():
        succeed()

    @task(task_id="fraud_check")
    def fraud_check():
        succeed()

    @task(task_id="inventory_check")
    def inventory_check():
        succeed()

    @task(task_id="ship_order",trigger_rule=TriggerRule.ALL_SUCCESS)
    def ship_order():
        succeed()

    start_task = start()
    payment_task = payment()
    fraud_check_task = fraud_check()
    inventory_check_task = inventory_check()
    ship_order_task = ship_order()

    start_task >> [payment_task,fraud_check_task,inventory_check_task] >> ship_order_task

triggers_pipeline()    

     