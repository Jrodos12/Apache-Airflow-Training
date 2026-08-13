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
def filter_two_seaters(json_data:str):
    df = pd.read_json(StringIO(json_data))

    two_seater_df = df[df["Seats"] == 2]

    return {'result': two_seater_df.to_json(),'filename':'two_seaters'}

def filter_fwds(json_data:str):
    df = pd.read_json(StringIO(json_data))

    fwds_df = df[df['PowerTrain'] == "FWD"]

    return {'result': fwds_df.to_json(), 'filename': 'fwds'}

def write_csv_result(fwds_data=None, two_seaters_data=None):
    jsondata = ( fwds_data['result'] or two_seaters_data['result'])

    file_name = (fwds_data['filename'] or two_seaters_data['filename'])

    df = pd.read_json(StringIO(jsondata))
    df.to_csv(
        os.path.join(os.getenv('CARS_OUTPUT'),f'{file_name}.csv'),index=False
    )

