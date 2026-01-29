from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime

with DAG(
    dag_id="pipeline_master_full",
    start_date=datetime(2024,1,1),
    schedule="@daily",
    catchup=False,
    tags=["pipeline"]
) as dag:

    bronze = TriggerDagRunOperator(
        task_id="trigger_bronze",
        trigger_dag_id="bronze_upload_to_s3"
    )

    silver = TriggerDagRunOperator(
        task_id="trigger_silver",
        trigger_dag_id="silver_load_to_rds"
    )

    gold = TriggerDagRunOperator(
        task_id="trigger_gold",
        trigger_dag_id="gold_transformations"
    )

    bronze >> silver >> gold
