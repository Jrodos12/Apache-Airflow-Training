from datetime import datetime,timedelta
from airflow.sdk import task,dag
from airflow.providers.standard.sensors.filesystem import FileSensor

default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}
@dag ('first_sensor_file',
    description="A dag that has a fileSensor",
    schedule='@once',
    catchup=False,
    tags=['workflow_api','sensor','decorators'],
    default_args=default_args
)
def sensor_file():
    checking_file = FileSensor(task_id='check_file',
                               fs_conn_id='fs_default',
                               filepath='tmp/laptops.csv',
                               poke_interval=10,
                               timeout= 60 * 10,
                               mode='poke')

sensor_file()