# Avance 3 - Transformación de Datos y Construcción del Data Warehouse

## 📌 Contexto del Avance

En este avance se desarrolló la capa de **transformación de datos (Silver)** y la **capa analítica final (Gold)** del Data Warehouse.  
Se integraron datos estructurados (CSV) y no estructurados (JSON) con el objetivo de generar tablas optimizadas para análisis de negocio.

Este proceso sigue la arquitectura **ELT**, donde los datos se cargan primero en su forma bruta (Bronze) y posteriormente se transforman dentro del Data Warehouse mediante SQL.

---

## 🎯 Objetivos del Avance

- Transformar los datos cargados en la capa Bronze hacia una estructura limpia y normalizada.
- Integrar los datos de Airbnb con las tasas de cambio provenientes de la API.
- Construir un modelo dimensional tipo **Star Schema** (Dimensiones + Tabla de Hechos).
- Crear una capa **Gold (Data Mart)** para análisis de negocio.
- Generar consultas SQL para responder preguntas estratégicas del negocio.

---

## 🏗️ Arquitectura del Data Warehouse

El Data Warehouse se estructuró en **tres capas**:

### 🥉 Bronze (Raw)

Datos originales sin transformación provenientes de:

- CSV de Airbnb
- JSON de tasas de cambio

### 🥈 Silver (Clean & Integrated)

- Limpieza de datos erróneos
- Conversión de tipos de datos
- Integración con tasas de cambio
- Enriquecimiento de precios en USD, MXN y ARS

### 🥇 Gold (Analytics)

- Modelo dimensional optimizado
- Tabla maestra para consultas analíticas

---

## 📂 Archivos Implementados

### 🐍 Scripts de Carga a RDS

| Archivo                | Descripción                                           |
| ---------------------- | ----------------------------------------------------- |
| `load_airbnb_env.py`   | Carga el CSV de Airbnb desde S3 a MySQL RDS           |
| `load_exchange_env.py` | Carga el JSON de tasas de cambio desde S3 a MySQL RDS |

---

### 🗄️ Scripts SQL del Data Warehouse

| Archivo                 | Descripción                                       |
| ----------------------- | ------------------------------------------------- |
| `gold_layer.sql`        | Transformación Silver + Modelo Dimensional + Gold |
| `preguntas_negocio.sql` | Consultas de negocio                              |

---

## 🧩 Transformaciones Implementadas (Silver Layer)

Se creó la tabla **airbnb_silver** con:

- Conversión de precios a DECIMAL
- Eliminación de registros con precios inválidos
- Integración con tasas de cambio más recientes
- Conversión automática de precios a:
  - USD
  - MXN
  - ARS
