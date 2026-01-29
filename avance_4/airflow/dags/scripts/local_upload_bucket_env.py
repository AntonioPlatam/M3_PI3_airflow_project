import boto3
import os
from datetime import datetime, UTC
from dotenv import load_dotenv


# ======================
# CONFIGURACIÓN
# ======================
load_dotenv()

S3_BUCKET = os.getenv("S3_BUCKET")
S3_PREFIX = os.getenv("S3_PREFIX")

CSV_LOCAL_PATH = os.getenv("CSV_LOCAL_PATH")

AWS_REGION = os.getenv("AWS_REGION")

# ======================
# FUNCIÓN
# ======================
def upload_csv_to_s3(local_path):
    if not os.path.exists(local_path):
        raise FileNotFoundError(f"No existe el archivo: {local_path}")

    s3 = boto3.client("s3", region_name=AWS_REGION)

    file_name = os.path.basename(local_path)
    s3_key = f"{S3_PREFIX}/{file_name}"

    s3.upload_file(
        Filename=local_path,
        Bucket=S3_BUCKET,
        Key=s3_key,
        ExtraArgs={"ContentType": "text/csv"}
    )

    return s3_key

# ======================
# MAIN
# ======================
if __name__ == "__main__":
    s3_path = upload_csv_to_s3(CSV_LOCAL_PATH)
    print(f"CSV subido correctamente a S3: s3://{S3_BUCKET}/{s3_path}")
