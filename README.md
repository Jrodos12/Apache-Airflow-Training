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
~~~
