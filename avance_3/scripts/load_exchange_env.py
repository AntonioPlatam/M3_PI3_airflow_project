import os
import json
import boto3
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# ======================
# CARGAR VARIABLES .env
# ======================
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY_RATES")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# ======================
# CLIENTES
# ======================
s3 = boto3.client("s3", region_name=AWS_REGION)

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ======================
# MAIN
# ======================
def main():
    obj = s3.get_object(Bucket=S3_BUCKET, Key=S3_KEY)
    data = json.loads(obj["Body"].read())

    record = {
        "base_currency": data["base"],
        "mxn_rate": float(data["rates"]["MXN"]),
        "ars_rate": float(data["rates"]["ARS"]),
        "rate_timestamp": data["timestamp"]
    }

    df = pd.DataFrame([record])
    df["rate_timestamp"] = pd.to_datetime(df["rate_timestamp"])

    df.to_sql(
        name="exchange_rates",
        con=engine,
        if_exists="append",
        index=False
    )

    print("✅ exchange_rates cargada correctamente")

if __name__ == "__main__":
    main()
