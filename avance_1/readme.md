# Avance 1 – Diseño de la Arquitectura del Pipeline ELT

## 📌 Contexto del Proyecto

Este proyecto corresponde al **Proyecto Integrador del módulo de Data Engineering**, cuyo objetivo es diseñar e implementar un **pipeline ELT escalable y un Data Warehouse en la nube**.

El rol asumido es el de **Ingeniero de Datos**, responsable de definir la arquitectura del sistema que permitirá integrar, transformar y analizar grandes volúmenes de datos provenientes de múltiples fuentes.

El caso de estudio se centra en el análisis del mercado de hospedaje (Airbnb NYC), con el fin de responder preguntas de negocio relacionadas con precios, demanda y comportamiento de hosts.

---

## 🎯 Objetivo del Pipeline ELT

Diseñar una arquitectura escalable que permita:

- Ingerir datos desde múltiples fuentes (CSV y APIs).
- Almacenar los datos crudos en una capa Raw.
- Transformar los datos en un Data Warehouse estructurado por capas.
- Automatizar el flujo con Apache Airflow.
- Implementar CI/CD con GitHub Actions.
- Garantizar calidad, trazabilidad y reproducibilidad del pipeline.

---

## 🔄 Enfoque ELT (Extract, Load, Transform)

El pipeline sigue la metodología **ELT**, donde los datos se cargan primero en bruto y luego se transforman dentro del ecosistema de datos.

### 🔹 Extract

Fuentes de datos utilizadas:

- Archivo CSV: `AB_NYC.csv` (dataset de Airbnb NYC).
- API externa de tasas de cambio (CurrencyFreaks).

La extracción se realiza mediante scripts en Python, ejecutados dentro de contenedores Docker.

---

### 🔹 Load

Los datos extraídos se almacenan en **Amazon S3 (capa Bronze)** sin transformaciones, conservando el formato original.

Propósito:

- Preservar el dato original.
- Permitir reprocesamiento futuro.
- Garantizar trazabilidad.

---

### 🔹 Transform

Las transformaciones se realizan en **Amazon RDS (MySQL)** estructurando los datos en capas:

| Capa   | Tecnología | Descripción                                 |
| ------ | ---------- | ------------------------------------------- |
| Bronze | Amazon S3  | Datos crudos sin transformar                |
| Silver | Amazon RDS | Datos limpios y normalizados                |
| Gold   | Amazon RDS | Datos agregados y optimizados para análisis |

---

## 🏗️ Arquitectura General del Pipeline

La arquitectura del pipeline está compuesta por los siguientes componentes:

1. **Fuentes de Datos**
   - CSV local (Airbnb NYC)
   - API externa de tasas de cambio

2. **Ingesta**
   - Scripts en Python
   - Contenedores Docker

3. **Almacenamiento Raw**
   - Amazon S3 (Bronze Layer)

4. **Transformación y Data Warehouse**
   - Amazon RDS MySQL
   - Capas Silver y Gold

5. **Orquestación**
   - Apache Airflow para automatizar el pipeline

6. **CI/CD**
   - GitHub Actions para automatizar pruebas y despliegue

7. **Consumo**
   - Jupyter Notebook para análisis y dashboards

---

## 🧱 Capas del Data Warehouse

### 🥉 Bronze Layer (Raw)

- Servicio: Amazon S3
- Contenido: Datos crudos CSV y JSON
- Pr
