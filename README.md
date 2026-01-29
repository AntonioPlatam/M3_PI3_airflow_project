# 🚀 Proyecto Integrador - Pipeline ELT y Data Warehouse Escalable

## 📌 Contexto del Proyecto

Como Ingeniero de Datos en una empresa en expansión, se diseñó e implementó un pipeline de datos tipo **ELT (Extract, Load, Transform)** desplegado en la nube.  
El objetivo del proyecto es integrar múltiples fuentes de datos, transformarlas y almacenarlas en un **Data Warehouse escalable en capas**, orquestado con **Apache Airflow** y automatizado mediante **GitHub Actions (CI/CD)**.

---

## 🎯 Objetivos del Proyecto

- Diseñar e implementar un pipeline ELT en batch.
- Integrar datos desde múltiples fuentes (CSV y API).
- Construir un Data Warehouse en capas (Bronze, Silver, Gold).
- Aplicar transformaciones mediante SQL.
- Orquestar el pipeline con Apache Airflow.
- Implementar CI/CD con GitHub Actions.
- Generar análisis y dashboard en Jupyter Notebook.

---

## 🏗️ Arquitectura del Pipeline

**Fuentes de Datos → S3 (Bronze) → MySQL RDS (Silver & Gold) → Analytics Notebook**

### Capas del Data Warehouse

| Capa       | Descripción                                 |
| ---------- | ------------------------------------------- |
| **Bronze** | Datos crudos almacenados en S3 (CSV y JSON) |
| **Silver** | Datos limpiados y transformados en MySQL    |
| **Gold**   | Modelo dimensional optimizado para análisis |

---

## 🛠️ Tecnologías Utilizadas

- Python
- AWS S3
- AWS RDS MySQL
- Apache Airflow
- Docker & Docker Compose
- SQL (MySQL)
- GitHub Actions (CI/CD)
- Jupyter Notebook

---

## ⚙️ Pipeline ELT

### 1️⃣ Extract & Load (Bronze)

- Extracción de datos desde:
  - Dataset Airbnb NYC (CSV)
  - API de tasas de cambio (JSON)
- Almacenamiento en AWS S3.

### 2️⃣ Transform & Load (Silver)

- Limpieza y normalización de datos.
- Conversión de precios a múltiples monedas.
- Carga a MySQL RDS.

### 3️⃣ Data Warehouse (Gold)

- Modelo dimensional tipo Star Schema:
  - Tablas Dimensionales
  - Tabla de Hechos
  - Data Mart final para analítica

---

## 📊 Análisis de Negocio

Se responden preguntas estratégicas como:

- ¿Cuáles son las zonas más rentables?
- ¿Cuál es el precio promedio por barrio?
- ¿Qué tipo de alojamiento es más demandado?
- ¿Quiénes son los hosts con mayor número de propiedades?

---

## 🤖 Orquestación y CI/CD

### Apache Airflow

- DAGs definidos para:
  - Ingesta
  - Transformación
  - Carga en Data Warehouse

### GitHub Actions

- Pipeline CI/CD para:
  - Validación de código
  - Linting
  - Automatización de despliegues

---

## 📈 Dashboard

Se desarrolló un notebook en **Jupyter Notebook** que consulta el Data Warehouse y genera visualizaciones para responder preguntas de negocio.

---

## 👤 Autor

**Antonio Plata**  
Bootcamp Data Engineer - Henry

## 📂 Estructura del Proyecto

```text
airflow_project/
│
├── dags/                  # DAGs de Apache Airflow
│   ├── bronze_upload_dag.py
│   ├── silver_load_dag.py
│   └── gold_transform_dag.py
│
├── scripts/               # Scripts Python de ingestión y carga
│   ├── api_aws_bucket_env.py
│   ├── local_upload_bucket_env.py
│   ├── load_airbnb_env.py
│   └── load_exchange_env.py
│
├── sql/                   # Scripts SQL del Data Warehouse
│   └── gold_layer.sql
│
├── notebooks/             # Dashboard y análisis
│   └── analysis.ipynb
│
├── docs/                  # Documentación por avances
│   ├── avance_1_ingestion.md
│   ├── avance_2_etl_pipeline.md
│   ├── avance_3_data_warehouse.md
│   └── avance_4_analytics.md
│
├── docker-compose.yml     # Infraestructura Airflow
├── Dockerfile              # Contenerización de scripts
├── .env.example            # Variables de entorno ejemplo
├── .gitignore

---
```
