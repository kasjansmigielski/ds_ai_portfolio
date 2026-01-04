# Job Seeker Agents

<div class="project-meta" markdown>
**Role:** AI Engineer / Full-Stack Developer  
**Period:** December 2025 – present  
**Status:** 🟢 Active Development  
</div>

---

## Project description

**Job Seeker Agents** is a multi-agent AI system for automating the job search process with a **human-in-the-loop workflow**.

Looking for a job in AI/ML is a **time-consuming and repetitive process**:

- Daily browsing of multiple job portals
- Manually evaluating offer-to-skills fit
- Customizing CV for each offer separately
- Lack of systematic application tracking
- Wasting time on irrelevant offers

The system combines:

- **Automatic** job scraping and triaging
- **Intelligent** CV tailoring per offer and company
- **Transparent** workflow with Trello as the interface
- **Full control** — the candidate approves every step
- **Tracing** — every agent decision is visible

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        JOB SEEKER AGENTS                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐             │
│  │   SCRAPER   │───▶│   TRIAGE    │───▶│  CV TAILOR  │             │
│  │  (JustJoin) │    │   AGENT     │    │    AGENT    │             │
│  └─────────────┘    └─────────────┘    └─────────────┘             │
│        │                  │                   │                     │
│        ▼                  ▼                   ▼                     │
│  ┌─────────┐        ┌─────────────────────────────┐                │
│  │  SQLite │        │  FIT / MAYBE / SKIP         │                │
│  │   DB    │        │  → Trello Board             │                │
│  └─────────┘        └──────────────┬──────────────┘                │
│                                    │                                │
│                                    ▼                                │
│              ┌───────────────────────────────────┐                  │
│              │         CV TAILOR AGENT           │                  │
│              │       (OpenAI Agents SDK)         │                  │
│              ├───────────────────────────────────┤                  │
│              │ • About Me + Company name         │                  │
│              │ • Tailored Skills                 │                  │
│              │ • Tailored Experience             │                  │
│              │ • Selected Projects               │                  │
│              │ • ATS Keywords                    │                  │
│              └───────────────┬───────────────────┘                  │
│                              ▼                                      │
│              ┌───────────────────────────────────┐                  │
│              │         REVIEW AGENT              │                  │
│              │ • TL;DR of the offer              │                  │
│              │ • Strengths/Weaknesses            │                  │
│              │ • Interview tips                  │                  │
│              └───────────────┬───────────────────┘                  │
│                              ▼                                      │
│              ┌───────────────────────────────────┐                  │
│              │  📎 CV PDF → Trello attachment    │                  │
│              │  📋 Review → Trello comment       │                  │
│              └───────────────────────────────────┘                  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                 OBSERVABILITY (Langfuse)                     │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Multi-Agent System

### Triage Agent

**Role:** First line of offer evaluation

**Input:** Raw job offer (title, description, stack, location)

**Output:** 

- Score 0-100
- Category: FIT (80+) / MAYBE (50-79) / SKIP (<50)
- Justification

**Technology:** OpenAI Responses API

---

### CV Tailor Agent

**Role:** CV personalization for a specific offer and company

**Input:** 

- Job offer
- Master Profile from Obsidian (skills, projects, experience)

**Output:**

- **About Me** — with company name (e.g., "I would thrive at Trans.eu...")
- **Key Achievements** — 5-6 bullets with metrics
- **Tailored Skills** — 10-15 most relevant
- **Tailored Experience** — Gotoit/Capgemini descriptions tailored to the offer
- **Tailored Projects** — 3-5 with offer-specific descriptions
- **ATS Keywords** — 10-15 keywords

**Technology:** OpenAI Agents SDK with tracing

**Key feature:** Dynamic experience description adaptation:

- Offer requires ML → highlight RAG project at Gotoit
- Offer requires CV/DL → highlight CNN at Capgemini
- Offer requires Cloud → highlight DigitalOcean, AWS cert
- Offer requires MLOps → highlight LLMOps in AInnouncer

---

### Review Agent

**Role:** Interview preparation

**Input:** Offer + triage result + master profile

**Output:**

- **TL;DR** — 2-3 sentences about the offer essence
- **Key requirements** — 3-4 points
- **Strengths** — with portfolio evidence
- **Weaknesses** — with suggestions how to address
- **Interview tips** — what to prepare
- **Questions for recruiter** — 2-3 intelligent questions

---

## Key Features

### 1. Human-in-the-Loop Workflow

Trello as the candidate interface:

- Offers automatically appear on the board
- Candidate sees score and justification
- Can move cards between lists
- CV is generated for offers from specific lists

### 2. Obsidian Integration

Master Profile in Obsidian as **single source of truth**:

- Skills, projects, experience in one place
- Agent reads data dynamically
- Profile update = better CV

### 3. Full Tracing

Every agent decision is traced:

- OpenAI Agents SDK tracing
- Langfuse integration
- Ability to debug "why did the agent choose this skill?"

### 4. No Hallucinations Policy

Agents **don't make things up**:

- Skills only from candidate's list
- Project technologies only from original descriptions
- Experience only from master-profile

---

## What I did

1. Designed **multi-agent architecture** with human-in-the-loop
2. Implemented **Triage Agent** with Responses API
3. Built **CV Tailor Agent** with OpenAI Agents SDK
4. Created **Review Agent** for interview preparation
5. Integrated with **Trello API** (cards, comments, attachments)
6. Connected with **Obsidian vault** as source of truth
7. Built **React frontend** for CV preview and configuration
8. Implemented **PDF generation** with React PDF Renderer
9. Configured **tracing and observability** with Langfuse

---

## Skills

<div class="skills-grid" markdown>

| Category | Technologies |
|----------|--------------|
| **AI/LLM** | OpenAI GPT-4o, OpenAI Agents SDK, RAG |
| **Backend** | Python, FastAPI, Pydantic, SQLite |
| **Frontend** | React, TypeScript, Next.js, Tailwind CSS |
| **Integrations** | Trello API, Obsidian, JustJoin.it |
| **DevOps** | Docker, Langfuse |

</div>

---

## Results

- ✅ Automation of 80% of the job search process
- ✅ CV personalized in < 30 seconds
- ✅ Full control over the process (human-in-the-loop)
- ✅ Tracing of every agent decision
- ✅ Zero hallucinations — only real skills
- ✅ Ready PDF with Trello attachment
