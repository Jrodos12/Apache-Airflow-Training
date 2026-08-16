from datetime import datetime, timedelta
from airflow.sdk import dag,task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import os
from dotenv import load_dotenv
from src.saves_db_data_to_csv import *
load_dotenv()

default_args = {
    'owner': 'jrodo',
    'start_date': datetime(2024, 6, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

@dag(
    'Postgresql_task',
    description='Using sql operator to perfom task with a DB',
    schedule=None,
    catchup=False,
    default_args = default_args,
    tags=['postgres', 'sql'],
    template_searchpath=os.getenv('QUERY_PATH')
)
def performn_queries():
    create_customer_purchase_table = SQLExecuteQueryOperator(
        task_id="Create_customer_table",
        conn_id="postgres_conection",
        sql='create_table_customer_purchase.sql'
    )

    create_customer_table = SQLExecuteQueryOperator(
        task_id="Create_customer_purchase_table",
        conn_id="postgres_conection",
        sql='create_table_customer.sql'
    )

    insert_customers = SQLExecuteQueryOperator(
        task_id="insert_customers",
        conn_id="postgres_conection",
        sql='insert_customers.sql'
    )

    insert_customers_purchase = SQLExecuteQueryOperator(
        task_id="insert_customers_purchase",
        conn_id="postgres_conection",
        sql='insert_customers_purcharse.sql'
    )

    create_join_table = SQLExecuteQueryOperator(
        task_id="create_join_table",
        conn_id="postgres_conection",
        sql='join_customers_table.sql'
    )

    filter_complete_table = SQLExecuteQueryOperator(
        task_id="filter_join_table",
        conn_id="postgres_conection",
        sql='filter_join_table.sql',
        parameters = {'lower': 5 , 'upper': 9},
        do_xcom_push=True
    )

    @task(task_id='export_db_data')
    def export_data(filter_data:list):
        export_csv(filter_data=filter_data)

    create_customer_table >> create_customer_purchase_table >> insert_customers >> insert_customers_purchase \
    >> create_join_table >> filter_complete_table >> export_data(filter_complete_table.output)

performn_queries()

