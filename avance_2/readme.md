# Avance 2 – Extracción e Ingesta de Datos (ELT Pipeline)

## 📌 Contexto del Avance

En este avance se desarrolló la **fase de extracción e ingesta de datos** del pipeline ELT, integrando múltiples fuentes externas y cargándolas en la capa **Bronze (Raw)** del Data Warehouse.

Se implementaron scripts en Python para:

- Extraer datos desde una API pública de tasas de cambio.
- Cargar un dataset CSV de Airbnb NYC desde almacenamiento local.
- Subir ambos datasets a Amazon S3 (capa raw).
- Preparar la estructura de la base de datos en MySQL (RDS) para las siguientes etapas del pipeline.

---

## 🏗️ Arquitectura de Ingesta

Las fuentes de datos utilizadas fueron:

| Fuente             | Tipo | Descripción                                     |
| ------------------ | ---- | ----------------------------------------------- |
| Airbnb NYC Dataset | CSV  | Dataset público con información de alojamientos |
| CurrencyFreaks API | JSON | API de tasas de cambio (USD → MXN, ARS)         |

Flujo de datos implementado:

---

## 🧩 Scripts de Extracción e Ingesta

### 1️⃣ Subida de datos desde API a S3

**Archivo:** `scripts/api_aws_bucket_env.py`

Funciones principales:

- Llamada HTTP a la API de CurrencyFreaks.
- Transformación del JSON.
- Carga del archivo JSON a un bucket S3.
- Uso de variables de entorno para credenciales y configuración.

---

### 2️⃣ Subida de CSV local a S3

**Archivo:** `scripts/local_upload_bucket_env.py`

Funciones principales:

- Lectura del archivo CSV local.
- Carga directa a Amazon S3.
- Parametrización mediante variables de entorno.

---

## 🗄️ Capa Bronze – Estructura de Base de Datos

Se diseñó la capa **Bronze** en MySQL (RDS) para almacenar los datos en estado crudo.

**Archivo SQL:** `sql/data_raw.sql`

Tablas creadas:

### 🟤 `bronze_airbnb_raw`

Tabla para almacenar el dataset CSV sin transformar.

Campos principales:

- id
- name
- host_id
- neighbourhood_group
- price (string para evitar errores de calidad de datos)
- availability_365
- reviews_per_month

---

### 🟤 `bronze_exchange_rates_raw`

Tabla para almacenar tasas de cambio provenientes de la API.

Campos principales:

- base_currency
- mxn_rate
- ars_rate
- rate_timestamp
- loaded_at

---

## 🎯 Resultados del Avance

✔ Extracción automatizada de datos desde API  
✔ Carga de dataset CSV a Amazon S3  
✔ Diseño e implementación de la capa Bronze en MySQL  
✔ Parametrización con variables de entorno  
✔ Preparación para transformación en la capa Silver

---

## 🔜 Próximo Avance

En el siguiente avance se desarrollaron las transformaciones SQL para:

- Limpieza de datos
- Integración de tasas de cambio con Airbnb
- Creación de capas Silver y Gold
- Construcción del Data Warehouse analítico
