import os
import boto3
import pandas as pd
from io import BytesIO
from sqlalchemy import create_engine
from datetime import datetime, timezone
from dotenv import load_dotenv

# ======================
# CARGAR .env
# ======================
load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY_AIRBNB")

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
    df = pd.read_csv(BytesIO(obj["Body"].read()))

    print(f"📥 Registros leídos: {len(df)}")

    # Normalizar columnas
    df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]

    # Timestamp de ingesta
    df["ingestion_timestamp"] = datetime.now(timezone.utc)

    df.to_sql(
        name="airbnb_nyc",
        con=engine,
        if_exists="replace",  # cambia a append si luego haces incremental
        index=False
    )

    print("✅ airbnb_nyc cargada correctamente")

if __name__ == "__main__":
    main()
