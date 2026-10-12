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

## Arquitetura do Pipeline de Dados

O **Textile Intelligence Platform (TIP)** utiliza uma arquitetura de Engenharia de Dados baseada no modelo **Medallion (Bronze, Silver e Gold)**, transformando dados operacionais da indústria têxtil em informações confiáveis para análise e tomada de decisão.

### Fluxo de processamento

```text
              DADOS DA INDÚSTRIA TÊXTIL
                         |
                         v
                  BRONZE LAYER
                 Dados CSV brutos
                         |
                         v
                 PYTHON + PANDAS
                  Data Ingestion
                         |
                         v
                   DATA QUALITY
             Validação e consistência
                         |
                         v
                  TRANSFORMATION
             Normalização e tipagem
                         |
                         v
                   SILVER LAYER
               Dados limpos e tratados
                         |
              +----------+----------+
              |                     |
              v                     v
          POSTGRESQL           GOLD LAYER
       Persistência SQL      Agregações por setor
              |                     |
              v                     v
          FASTAPI              INDICADORES
         API REST              Quantidade de máquinas
                               Status operacional
                               Capacidade nominal
```

### Tecnologias utilizadas

| Tecnologia | Responsabilidade |
|---|---|
| Python + Pandas | Ingestão, qualidade e transformação |
| PostgreSQL | Persistência e consultas SQL |
| SQLAlchemy | Integração Python com banco de dados |
| Alembic | Versionamento do esquema do banco |
| FastAPI | Disponibilização de dados via API REST |
| Docker + Docker Compose | Conteinerização da aplicação e do banco |
| Pytest | Testes automatizados das regras Gold |

### Indicadores implementados na camada Gold

A primeira tabela analítica, `machine_sector_summary`, apresenta uma linha por setor industrial, contendo:

- Quantidade total de máquinas.
- Máquinas em operação (`Running`).
- Máquinas em manutenção (`Maintenance`).
- Máquinas paradas (`Stopped`).
- Capacidade horária nominal total.
- Capacidade horária nominal média.

Os indicadores foram validados por meio de agregações independentes em **Pandas e SQL/PostgreSQL**.

### Próxima evolução

Expansão do modelo de dados para integrar **máquinas, produção, ordens de produção, estoque, manutenção e qualidade**, preparando o TIP para processamento distribuído com PySpark, Databricks e Delta Lake.

## 👨‍💻 Author

Fernando Caruzo Bento
