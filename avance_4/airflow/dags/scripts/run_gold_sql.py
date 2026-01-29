import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

with open("/opt/airflow/dags/sql/gold_layer.sql") as f:
    sql = f.read()

cursor = conn.cursor()
for statement in sql.split(";"):
    if statement.strip():
        cursor.execute(statement)

conn.commit()
cursor.close()
conn.close()

print("✅ GOLD layer ejecutada")
