from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="silver_load_to_rds",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False,
    tags=["silver"]
) as dag:

    load_csv = BashOperator(
        task_id="load_airbnb_rds",
        bash_command="python /opt/airflow/dags/scripts/load_airbnb_env.py"
    )

    load_json = BashOperator(
        task_id="load_exchange_rds",
        bash_command="python /opt/airflow/dags/scripts/load_exchange_env.py"
    )

    load_csv >> load_json
