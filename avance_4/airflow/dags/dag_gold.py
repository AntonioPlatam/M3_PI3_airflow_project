from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="gold_transformations",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False,
    tags=["gold"]
) as dag:

    run_gold = BashOperator(
        task_id="run_gold_sql",
        bash_command="python /opt/airflow/dags/scripts/run_gold_sql.py"
    )
