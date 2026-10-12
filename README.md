# Textile Intelligence Platform

> Data Engineering, Machine Learning and Generative AI Platform for Textile Manufacturing.

## 📌 Overview

The Textile Intelligence Platform (TIP) is an end-to-end portfolio project that demonstrates modern Data Engineering, Machine Learning, MLOps and Generative AI practices applied to the textile industry.

The project simulates a real industrial environment, from data ingestion to AI-powered decision support.

---

## 🎯 Goals

* Build a modern Data Platform
* Develop scalable ETL pipelines
* Apply Data Quality concepts
* Create a Lakehouse architecture
* Train Machine Learning models
* Deploy production-ready APIs
* Implement MLOps best practices
* Build AI Agents and RAG applications

---

## 🛠 Planned Tech Stack

### Foundation

* Python
* Pandas
* SQL
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Docker
* Docker Compose
* Git & GitHub

### Data Engineering

* Apache Spark
* PySpark
* Databricks
* Delta Lake
* Airflow

### Machine Learning

* Scikit-Learn
* XGBoost
* MLflow

### Generative AI

* OpenAI
* LangChain
* LangGraph
* RAG
* Vector Database

---

## 🚀 Project Status

🟡 In Development

### Current Architecture

The project currently implements an end-to-end data pipeline for textile machine data:

**CSV / Raw Data → Data Ingestion → Data Quality Validation → Data Transformation → Idempotent Load / Upsert → PostgreSQL → FastAPI → REST API / JSON**

The application and PostgreSQL database run as separate Docker containers orchestrated with Docker Compose.

Database schema evolution is managed with Alembic.

### ✅ Completed

* Project foundation
* FastAPI initial setup
* CSV data ingestion with Pandas
* Data Quality validation
* Data transformation and type normalization
* SQLAlchemy database layer
* Machine data model
* Database migrations with Alembic
* Idempotent data loading / Upsert
* PostgreSQL persistence
* FastAPI database dependency
* REST endpoint for machine data
* Dockerized FastAPI application
* Dockerized PostgreSQL database
* Multi-container environment with Docker Compose
  - Estruturação do Data Lake em camadas Bronze, Silver e Gold
- Implementação da camada Bronze para armazenamento dos dados brutos
- Implementação da camada Silver com dados tratados e validados
- Implementação da camada Gold com indicadores agregados por setor
- Cálculo de métricas de máquinas: quantidade, status e capacidade produtiva nominal
- Validação dos indicadores Gold utilizando SQL no PostgreSQL
- Integração automática das camadas Bronze → Silver → Gold ao pipeline de dados
- Testes automatizados da camada Gold utilizando pytest
- Validação da execução idempotente do pipeline
- Padronização do ambiente Python 3.12 e das dependências do projeto

---

## 📅 Roadmap

### Foundation & Data Engineering

* [x] Project structure
* [x] FastAPI foundation
* [x] CSV data ingestion
* [x] Data Quality validation
* [x] Data transformation
* [x] SQLAlchemy ORM
* [x] Database migrations with Alembic
* [x] Idempotent data loading / Upsert
* [x] PostgreSQL
* [x] Docker & Docker Compose
* [x] REST API for machine data

### Next Steps

* [ ] Expand industrial datasets
* [ ] Data Lake
* [ ] Apache Spark / PySpark
* [ ] Databricks
* [ ] Delta Lake
* [ ] Lakehouse architecture
* [ ] Analytics / SQL
* [ ] Machine Learning
* [ ] MLflow / MLOps
* [ ] Generative AI / RAG
* [ ] Cloud Infrastructure
* [ ] Terraform

---

## 👨‍💻 Author

Fernando Caruzo Bento
