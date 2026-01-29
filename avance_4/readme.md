# Avance 4 – Orquestación del Pipeline y CI/CD

## 📌 Contexto del Avance

En este avance se implementó la orquestación completa del pipeline ELT utilizando Apache Airflow, junto con la contenerización mediante Docker y la automatización de pruebas mediante GitHub Actions.

El objetivo fue automatizar la ejecución del pipeline desde la ingesta de datos hasta la generación de la capa Gold, garantizando reproducibilidad, escalabilidad y mantenibilidad.

---

## 🐳 Contenerización del Pipeline con Docker

Se configuró un entorno completo de Apache Airflow utilizando Docker Compose y un Dockerfile personalizado.

### 📂 Archivos Implementados

| Archivo              | Descripción                                        |
| -------------------- | -------------------------------------------------- |
| `docker-compose.yml` | Infraestructura de Airflow con PostgreSQL y Redis  |
| `Dockerfile`         | Imagen personalizada con dependencias del pipeline |

---

## ⏱️ Orquestación con Apache Airflow

Se definieron DAGs modulares para cada capa del Data Warehouse, siguiendo la arquitectura ELT.

### 🧩 DAGs Implementados

| DAG                      | Descripción                                         |
| ------------------------ | --------------------------------------------------- |
| `dag_bronze.py`          | Ingesta de datos desde API y CSV hacia S3 (Bronze)  |
| `dag_silver.py`          | Carga de datos desde S3 hacia RDS MySQL (Silver)    |
| `dag_gold.py`            | Transformaciones SQL y creación de Data Mart (Gold) |
| `dag_pipeline_master.py` | Orquestador maestro del pipeline completo           |

---

### 🧠 Flujo del Pipeline

1. **Bronze Layer**
   - Extracción de datos desde API (CurrencyFreaks)
   - Carga del dataset Airbnb desde archivo local
   - Persistencia en Amazon S3

2. **Silver Layer**
   - Lectura de archivos desde S3
   - Carga en MySQL RDS

3. **Gold Layer**
   - Transformaciones SQL
   - Modelo dimensional (Star Schema)
   - Creación de Big Table analítica

---

## 🗄️ Transformaciones Automatizadas

Se automatizó la ejecución del script SQL de la capa Gold utilizando Python.

### 📂 Archivo

| Archivo           | Descripción                                     |
| ----------------- | ----------------------------------------------- |
| `run_gold_sql.py` | Ejecuta `gold_layer.sql` en MySQL desde Airflow |

---

## 🔄 CI/CD con GitHub Actions

Se configuró un pipeline de integración continua para validar el código en cada push o pull request.

### 📂 Archivo

| Archivo                    | Descripción                          |
| -------------------------- | ------------------------------------ |
| `.github/workflows/ci.yml` | Pipeline CI para pruebas automáticas |

### 🧪 Validaciones Implementadas

- Instalación de dependencias Python
- Linting del código
- Validación de scripts Python y SQL

---

## 📊 Dashboard Analítico en Jupyter Notebook

Se desarrolló un Notebook para responder preguntas de negocio utilizando la capa Gold del Data Warehouse.

### 📂 Archivo

| Archivo       | Descripción                                             |
| ------------- | ------------------------------------------------------- |
| `final.ipynb` | Dashboard analítico con consultas SQL y visualizaciones |

---

## 📈 Preguntas de Negocio Respondidas

- Zonas más rentables de Nueva York
- Precio promedio por barrio
- Tipos de alojamiento más demandados
- Hosts con mayor número de propiedades

Las consultas se ejecutan sobre la tabla:

```sql
gold_airbnb_master
```
