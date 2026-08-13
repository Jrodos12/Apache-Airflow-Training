from airflow.sdk import  task,dag,setup,teardown
from datetime import datetime,timedelta
from src.conditional_task import *
default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

@dag('conditional_task_with_decorator',
    schedule='@once',
    catchup=False,
    tags=['workflow_api','conditional','decorators'],
    default_args=default_args
)
def conditional_decorators_pipeline():
    @setup
    def setting_enviroment_task():
        setting_eviroment()

    @teardown
    def cleaning_enviroment_task():
        cleaning_enviroment()

    @task.run_if(
        is_manual_run,skip_message="Skipped: triggers on manual executions"
    )
    @task(task_id='Heave_compliance_audit')
    def run_heavy_compliance_audit_task():
        compliance_audit()

    @task.skip_if(
        is_dry_run,skip_message="Skipped: No commit on dry run"
    )
    @task(task_id='data_to_warehouse',trigger_rule="none_failed")
    def commit_data_to_warehouse_task():
        data_to_warehouse()

    set_enviroment = setting_enviroment_task()
    clean_enviroment = cleaning_enviroment_task()

    with clean_enviroment.as_teardown(setups=set_enviroment):
        audit = run_heavy_compliance_audit_task()
        commit = commit_data_to_warehouse_task() 
        audit >> commit
conditional_decorators_pipeline()
        