from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="bronze_upload_to_s3",
    start_date=datetime(2024,1,1),
    schedule=None,
    catchup=False,
    tags=["bronze"]
) as dag:

    upload_api = BashOperator(
        task_id="upload_api_json",
        bash_command="python /opt/airflow/dags/scripts/api_aws_bucket_env.py"
    )

    upload_csv = BashOperator(
        task_id="upload_airbnb_csv",
        bash_command="python /opt/airflow/dags/scripts/local_upload_bucket_env.py"
    )

    upload_api >> upload_csv
