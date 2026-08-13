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

@dag('dependencies_with_taskflow_api_with_branches',
    default_args=default_args,
    schedule='@once',
    catchup=False,
    tags=['taskflow_api','branching'])
def branching_car_processing_data():
    @task(task_id='read_csv_file_task')
    def read_csv_file_task():
        return read_cvs_file()
    
    @task.branch(task_id='determine_branch_task')
    def determine_branch_task():
        return determine_branch()
    
    @task(task_id='filter_two_seaters_task')
    def filter_two_seaters_task(data):
        return filter_two_seaters(data)

    @task(task_id='filter_fwds_task')
    def filter_fwds_task(data):
        return filter_fwds(data)

    @task(task_id='write_csv_result_task',trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS)
    def write_csv_result_task(two_seats_data,fwds_data):
        write_csv_result(two_seats_data,fwds_data)

    csv_data = read_csv_file_task()
    branch = determine_branch_task()
    two_seaters_data = filter_two_seaters_task(csv_data)
    fwds_data = filter_fwds_task(csv_data)
    write_csv_result_task(two_seaters_data,fwds_data)
    csv_data >> branch >> [two_seaters_data,fwds_data]

branching_car_processing_data()