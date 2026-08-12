from airflow.sdk import Variable
import os
from dotenv import load_dotenv
import pandas as pd
from io import StringIO
load_dotenv()

def read_cvs_file():
    df = pd.read_csv(os.getenv('CARS_PATH'))
    return df.to_json()

def determine_branch():
    final_output = Variable.get("transform",default=None)
    if final_output == "filter_two_seaters":
        return "filter_two_seaters_task"
    elif final_output == "filter_fwds":
        return "filter_fwds_task"
    else:
        return ValueError(f"Uknow transform value: '{final_output}'")
def filter_two_seaters(ti):
    json_data = ti.xcom_pull(task_ids="read_csv_file_task")

    df = pd.read_json(StringIO(json_data))

    two_seater_df = df[df["Seats"] == 2]

    ti.xcom_push(key="transform_result", value=two_seater_df.to_json())
    ti.xcom_push(key="transform_filename", value="two_seaters")

def filter_fwds(ti):
    json_data = ti.xcom_pull(task_ids="read_csv_file_task")

    df = pd.read_json(StringIO(json_data))

    fwds_df = df[df['PowerTrain'] == "FWD"]

    ti.xcom_push(key="transform_result", value=fwds_df.to_json())
    ti.xcom_push(key="transform_filename", value="fwds")

def write_csv_result(ti):
    jsondata = ( ti.xcom_pull(task_ids="filter_two_seaters_task",key="transform_result") or
                 ti.xcom_pull(task_ids="filter_fwds_task",key="transform_result")
    )
    file_name = (ti.xcom_pull(task_ids="filter_two_seaters_task",key="transform_filename") or
                 ti.xcom_pull(task_ids="filter_fwds",key="transform_filename")
    )
    df = pd.read_json(StringIO(jsondata))
    df.to_csv(
        os.getenv('CARS_OUTPUT'),index=False
    )

