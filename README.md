# Apache-Airflow-Training
My repository for and intermediate level course of Apache Airflow
# Requirements
This repository need airflow 3.3+, python 3.14 
Execute
~~~
pip install -r requirements.txt
~~~
For install all the dependencies

# Usage
Copy the dags in the dag folder in your airflow dags folder and copy the airflow/src folder in you airflow folder.
## Enviroments variables
you  will need to update the next $variables to execute the dags:
~~~
export AIRFLOW__CORE__DAGS_FOLDER="absolute_path__for_the_dags_in_the_repository"
export PYTHONPATH="absolute_path__for_the_src_in_the_repository"
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW__CORE__TEST_CONNECTION=Enabled
export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow_user:password@127.0.0.1:5432/your airflow_db
QUERY_PATH="absolute path to query folder in the project"
CARS_PATH="aboslute_path to your cars csv file ...airflow/data/car_data.csv"
CARS_OUTPUT="aboslute_path to your output folder ...folder/airflow/data/"
OUTPUT_FOLDER="data"
DB_OUTPUT="aboslute_path to your output folder ....airflow/data/filter_data.csv"

~~~
