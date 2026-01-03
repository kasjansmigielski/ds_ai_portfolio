# Knowledge Seeker

*Project start: April 2025 — Present*

**Role:** AI / ML Engineer (Project Leader)

**Status:** Production

---

## Project description

<div style="text-align: justify;">
<strong>Knowledge Seeker</strong> is an advanced tool for transcription, indexing, and information retrieval from video recordings.

Users with access to large video resources (courses, trainings, mentoring sessions) had difficulty quickly finding specific information. Manually searching through hundreds of materials was time-consuming and inefficient.

<strong>As the project leader,</strong> I coordinate the development of a system utilizing the latest AI technologies for speech-to-text processing and implementation of advanced semantic search mechanisms.

The application enables users not only to find specific information in extensive video resources but also to generate responses to queries based on accumulated knowledge using the <strong>RAG (Retrieval-Augmented Generation) architecture</strong>.
</div>

---

## Solution

<div style="text-align: justify;">
I designed a system based on <strong>RAG (Retrieval-Augmented Generation)</strong> architecture, combining automatic video transcription, semantic search in a vector database, and response generation through language models.
</div>

---

## Architecture

![System architecture](data/architecture.png)

---

## Main functionalities

- Transcription of video recordings to text with preservation of time metadata (timestamps)
- Processing transcriptions through chunking and generating embeddings
- Vector database for storing and efficiently searching embeddings
- User interface enabling both simple and semantic content searching
- RAG (Retrieval-Augmented Generation) system for generating responses to user queries
- Deployment in Digital Ocean cloud ensuring scalability and availability
- Data export in JSON formats and streaming capability to user API

---

## What I did

1. Designed the system architecture and data processing pipeline
2. Implemented audio → text transcription using Whisper
3. Developed document chunking and embedding generation
4. Configured Qdrant vector database
5. Built backend API in FastAPI
6. Created user interface in Streamlit
7. Deployed the system in DigitalOcean cloud (Docker)

---

## Development Roadmap

- Integration with additional data sources (documents, presentations, audio)
- Enhancement of RAG mechanisms with advanced filtering and re-ranking techniques
- Implementation of components for automatic verification and updating of the knowledge base
- Optimization of indexing and search processes for larger datasets
- Development of API interface enabling integration with external applications

---

## Skills

- Python
- OpenAI
- Whisper
- Qdrant
- FastAPI
- Streamlit
- Docker
- DigitalOcean
- LLM (Large Language Models)
- Natural Language Processing
- Vector Databases
- RAG (Retrieval-Augmented Generation)
- Microservice Architecture

---

## Results

- **400+ video recordings** searchable in real-time
- Reduced information finding time from **minutes to seconds**
- Production-ready, scalable AI system
