# Quality Management System

*Project: February 2024 — August 2024*

**Role:** Data / AI Engineer

---

## Project description

In industrial organizations, quality and technical data are often **scattered across multiple sources**:

- quality reports in Excel,
- technical documentation in PDF,
- process instructions in various locations,
- corrective action history in separate files.

As a result:

- finding the right document takes too much time,
- data is inconsistent and difficult to compare,
- there's no single place for quality analysis and decisions,
- organizational knowledge is heavily dependent on specific people.

I designed the **Quality Management System (QMS)**, whose main goal was to create **one central source of truth** for quality data and technical knowledge.

---

## Solution

The system combines:

- classic QMS (reports, actions, metrics),
- **Knowledge Management** layer,
- **semantic search** enabling natural language queries.

Everything was delivered as a **Streamlit application** serving as an operational quality dashboard.

---

## Architecture Overview

QMS was designed as a system integrating multiple data sources:

- **Data ingestion** — import from PDF and Excel files, normalization and standardization
- **Central database** — relational database as single source of truth, unified quality data models
- **Knowledge layer** — document content extraction, embeddings and semantic index
- **Application layer** — Streamlit as user interface, dashboards, reports, search

The architecture was designed with:

- ERP / CRM integration in mind,
- future expansion with additional AI modules.

---

## Key Features

### Intelligent Semantic Search

- search drawings, instructions, and reports
- natural language queries
- no need to know folder structure

### Centralized & Standardized Data

- all quality data in one place
- consistent formats and current document versions
- elimination of duplicates and outdated files

### Automated Reporting & Analytics

- quality dashboards
- corrective action statuses
- quick quality KPI overview

### Integration-Ready Architecture

- preparation for ERP / CRM integration
- modular data structure
- readiness for further AI systems

---

## What I did

1. Analyzed existing quality data sources
2. Designed unified data model
3. Implemented data import and transformation from PDF and Excel
4. Created central database as single source of truth
5. Built semantic search layer over documentation
6. Developed quality dashboard in Streamlit
7. Automated reporting and action monitoring
8. Prepared architecture for future integrations and AI

---

## Skills

- Python
- Streamlit
- PostgreSQL
- Pandas
- SQL
- PDF Processing
- Excel Processing
- Semantic Search
- Embeddings
- Machine Learning
- Computer Vision
- Docker

---

## Results

- Reduced document search time by up to **70%**
- One consistent source of quality data
- Better process and action history transparency
- Faster quality decision-making
- Improved collaboration between:
  - production
  - quality
  - procurement
- Solid foundation for further AI system development in the organization
