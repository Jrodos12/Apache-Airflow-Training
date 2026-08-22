from datetime import datetime,timedelta
from airflow.sdk import task,dag
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from src.file_sensor_pipeline import *
import os
from dotenv import load_dotenv

load_dotenv()

default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
@dag ('sensor_pipeline',
    description="A dag that has a fileSensor",
    schedule=None,
    catchup=False,
    tags=['workflow_api','sensor','decorators'],
    default_args=default_args,
    template_searchpath=os.getenv('QUERY_PATH')
)
def sensor_file():

    create_laptos_table = SQLExecuteQueryOperator(
        task_id="Create_laptop_table",
        conn_id="laptop_db",
        sql='create_table_latop.sql'
    )

    @task(task_id='insert_laptop_data')
    def insert_laptop_data_task():
        insert_laptop_data()

    @task(task_id='filter_gaming_laptops')
    def filter_gaming_laptops_task():
        filter_gaming_laptops()

    @task(task_id='filter_notebook_laptops')
    def filter_notebook_laptops_task():
        filter_notebook_laptops()

    @task(task_id='filter_ultrabook_laptops')
    def filter_ultrabook_laptops_task():
        filter_ultrabook_laptops()

    checking_file = FileSensor(
        task_id='checking_for_file',
        filepath='tmp/laptops_*.csv',
        poke_interval=10,
        timeout=60 * 10,
        mode='reschedule'
    )


    create_laptos_table >> checking_file >> insert_laptop_data_task() >> [filter_gaming_laptops_task(), filter_notebook_laptops_task(),filter_ultrabook_laptops_task()]
sensor_file()