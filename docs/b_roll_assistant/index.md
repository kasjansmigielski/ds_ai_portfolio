# B-Roll Assistant

*Project start: October 2024 — Present*

**Role:** AI / Backend Engineer

---

## Project description

**B-Roll Assistant** is an intelligent AI assistant that **automatically catalogs video materials** and enables their **instant search**.

In newsrooms and video production environments, time is critical. Editors and video editors must **quickly find the right B-roll**, often under deadline pressure. In practice:

- video materials are poorly described or not at all,
- file names are ambiguous,
- manual tagging is costly and unrealistic,
- classic folder-based search doesn't scale.

The system:

- analyzes video without user intervention,
- generates snapshots and shot descriptions using AI,
- combines classic search with **semantic search**,
- learns from editor ratings.

Thanks to this, the editor doesn't need to know *how the file was named* — just describe **what they're looking for**.

---

## How It Works

### 1. Smart Catalog Setup

- System adapts to existing file structure
- No manual organization required
- Handles large B-roll archives

### 2. AI Shot Descriptions

- Automatic snapshot generation (FFmpeg)
- Visual shot analysis (AI Vision)
- Text descriptions for each clip: objects, scenes, context, atmosphere
- Each clip receives a **rich semantic description** without manual tagging

### 3. Dual Search & Continuous Learning

- **Keyword search** (fast, precise queries)
- **Semantic search** (search by meaning and concepts)

Example queries:

- "glass"
- "transparent container"
- "tense political rally"
- "crowd waiting nervously"

The system enables rating results, which:

- improves accuracy,
- adjusts ranking,
- increases search effectiveness over time.

---

## Architecture Overview

B-Roll Assistant is a **multimodal pipeline**:

- **Video ingestion** — file structure analysis, frame extraction
- **AI processing** — vision → image description, text → embeddings
- **Search layer** — classic indexes, vector database
- **Feedback loop** — user ratings, result ranking correction

Designed for **performance and scaling** in media environments.

---

## What I did

1. Designed the B-roll analysis system architecture
2. Implemented video frame extraction pipeline
3. Integrated AI Vision for shot analysis
4. Created automatic clip description system
5. Built **dual search engine** (keyword + semantic)
6. Deployed embedding-based search
7. Designed user feedback mechanism
8. Prepared backend API and data structure
9. Containerized the system (Docker)

---

## Skills

- Python
- OpenAI (Vision + LLM)
- Embeddings
- Vector Database
- FastAPI
- PostgreSQL
- FFmpeg
- Docker
- Semantic Search

---

## Results

- Find the right B-roll in **seconds instead of minutes**
- No need for manual tagging
- Better utilization of existing video archives
- System that **learns along with the editorial team**
- Solid foundation for: newsrooms, media houses, content platforms

---

## Sample photos

![Murawa search](data/murawa.png)
![Zabytki search](data/zabytki.png)
![File management](data/file_management.png)
![Drone footage](data/dron.png)
![Pisanie](data/pisanie.png)
