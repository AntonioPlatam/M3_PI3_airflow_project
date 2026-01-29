import os
import json
import requests
import boto3
from datetime import datetime, UTC
from dotenv import load_dotenv


# ======================
# CONFIGURACIÓN
# ======================
load_dotenv()
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

S3_BUCKET = os.getenv("S3_BUCKET")
S3_PREFIX = os.getenv("S3_PREFIX")
AWS_REGION = os.getenv("AWS_REGION")


# ======================
# FUNCIONES
# ======================

def get_exchange_rates():
    response = requests.get(API_URL, params={"apikey": API_KEY})
    response.raise_for_status()

    data = response.json()
    rates = data["rates"]

    return {
        "base": data["base"],
        "timestamp": datetime.now(UTC).isoformat(),
        "rates": {
            "MXN": rates.get("MXN"),
            "ARS": rates.get("ARS")
        }
    }

def upload_to_s3(data):
    s3 = boto3.client("s3", region_name=AWS_REGION)

    file_name = f"rates_{datetime.now(UTC).strftime('%Y%m%d_%H%M%S')}.json"
    s3_key = f"{S3_PREFIX}/{file_name}"

    s3.put_object(
        Bucket=S3_BUCKET,
        Key=s3_key,
        Body=json.dumps(data, indent=4),
        ContentType="application/json"
    )

    return s3_key
# ======================
# MAIN
# ======================
if __name__ == "__main__":
    exchange_rates = get_exchange_rates()
    s3_path = upload_to_s3(exchange_rates)
    print(f"Archivo subido correctamente a S3: s3://{S3_BUCKET}/{s3_path}")
