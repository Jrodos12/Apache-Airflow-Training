from airflow import DAG
from airflow.sdk import task,dag,TriggerRule
from datetime import datetime,timedelta
from src.procses_car_data_dependencies import read_cvs_file,write_csv_result,determine_branch,filter_fwds,filter_two_seaters

default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

@dag('Branching_using_taskflow_api',
    default_args=default_args,
    schedule='@once',
    catchup=False,
    tags=['taskflow_api','branching'])
def branching_car_processing_data():
    @task
    def read_csv_file_task():
        return read_cvs_file()
    @task.branch
    def determine_branch_task():
        return determine_branch()
    @task
    def filter_two_seaters_task(ti):
        filter_two_seaters(ti)
    @task
    def filter_fwds_task(ti):
        filter_fwds(ti)
    @task(trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS)
    def write_csv_result_task(ti):
        write_csv_result(ti)

    a = read_csv_file_task()
    b = determine_branch_task()
    c = filter_two_seaters_task()
    d = filter_fwds_task()
    e = write_csv_result_task()
    a >> b >> [c,d] >> e
branching_car_processing_data()