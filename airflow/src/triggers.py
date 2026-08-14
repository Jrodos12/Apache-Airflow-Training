from airflow.exceptions import AirflowSkipException
def succeed():
    print("Task Succeeded!")

def fail():
    raise ValueError("Task Failed!")

def skip():
    raise AirflowSkipException("Task Deliberately skipped")