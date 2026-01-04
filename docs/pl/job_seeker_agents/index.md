# Job Seeker Agents

<div class="project-meta" markdown>
**Rola:** AI Engineer / Full-Stack Developer  
**Okres:** Grudzień 2025 – obecnie  
**Status:** 🟢 Aktywny rozwój  
</div>

---

## Opis projektu

**Job Seeker Agents** to wieloagentowy system AI do automatyzacji procesu szukania pracy z **human-in-the-loop workflow**.

Szukanie pracy w branży AI/ML to **czasochłonny i powtarzalny proces**:

- Codzienne przeglądanie wielu portali z ofertami
- Ręczne ocenianie dopasowania oferty do umiejętności
- Dostosowywanie CV pod każdą ofertę osobno
- Brak systematycznego śledzenia aplikacji
- Utrata czasu na oferty, które nie pasują

System łączy:

- **Automatyczne** pobieranie i triażowanie ofert
- **Inteligentne** dopasowywanie CV do oferty i firmy
- **Przejrzysty** workflow z Trello jako interfejsem
- **Pełną kontrolę** — kandydat zatwierdza każdy krok
- **Tracing** — każda decyzja agenta jest widoczna

---

## Przegląd architektury

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
│  │   DB    │        │  → Tablica Trello           │                │
│  └─────────┘        └──────────────┬──────────────┘                │
│                                    │                                │
│                                    ▼                                │
│              ┌───────────────────────────────────┐                  │
│              │         CV TAILOR AGENT           │                  │
│              │       (OpenAI Agents SDK)         │                  │
│              ├───────────────────────────────────┤                  │
│              │ • About Me + nazwa firmy          │                  │
│              │ • Dopasowane Skills               │                  │
│              │ • Dopasowane Doświadczenie        │                  │
│              │ • Wybrane Projekty                │                  │
│              │ • ATS Keywords                    │                  │
│              └───────────────┬───────────────────┘                  │
│                              ▼                                      │
│              ┌───────────────────────────────────┐                  │
│              │         REVIEW AGENT              │                  │
│              │ • TL;DR oferty                    │                  │
│              │ • Mocne/Słabe strony              │                  │
│              │ • Tips do rozmowy                 │                  │
│              └───────────────┬───────────────────┘                  │
│                              ▼                                      │
│              ┌───────────────────────────────────┐                  │
│              │  📎 CV PDF → załącznik Trello     │                  │
│              │  📋 Review → komentarz Trello     │                  │
│              └───────────────────────────────────┘                  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                 OBSERVABILITY (Langfuse)                     │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## System wieloagentowy

### Triage Agent

**Rola:** Pierwsza linia oceny ofert

**Input:** Surowa oferta pracy (tytuł, opis, stack, lokalizacja)

**Output:** 

- Score 0-100
- Kategoria: FIT (80+) / MAYBE (50-79) / SKIP (<50)
- Uzasadnienie

**Technologia:** OpenAI Responses API

---

### CV Tailor Agent

**Rola:** Personalizacja CV pod konkretną ofertę i firmę

**Input:** 

- Oferta pracy
- Master Profile z Obsidian (skills, projekty, doświadczenie)

**Output:**

- **About Me** — z nazwą firmy (np. "I would thrive at Trans.eu...")
- **Key Achievements** — 5-6 bulletów z metrykami
- **Tailored Skills** — 10-15 najbardziej pasujących
- **Tailored Experience** — opisy Gotoit/Capgemini dopasowane do oferty
- **Tailored Projects** — 3-5 z opisami pod ofertę
- **ATS Keywords** — 10-15 słów kluczowych

**Technologia:** OpenAI Agents SDK z tracing

**Kluczowa cecha:** Dynamiczne dostosowywanie opisu doświadczenia:

- Oferta wymaga ML → podkreśl projekt RAG w Gotoit
- Oferta wymaga CV/DL → podkreśl CNN w Capgemini
- Oferta wymaga Cloud → podkreśl DigitalOcean, AWS cert
- Oferta wymaga MLOps → podkreśl LLMOps w AInnouncer

---

### Review Agent

**Rola:** Przygotowanie do rozmowy

**Input:** Oferta + wynik triage + master profile

**Output:**

- **TL;DR** — 2-3 zdania o istocie oferty
- **Kluczowe wymagania** — 3-4 punkty
- **Mocne strony** — z dowodami z portfolio
- **Słabe strony** — z sugestiami jak obejść
- **Tips do rozmowy** — co przygotować
- **Pytania do rekrutera** — 2-3 inteligentne pytania

---

## Kluczowe funkcje

### 1. Human-in-the-Loop Workflow

Trello jako interfejs dla kandydata:

- Oferty automatycznie trafiają na tablicę
- Kandydat widzi score i uzasadnienie
- Może przenosić karty między listami
- CV generowane jest dla ofert z określonych list

### 2. Integracja z Obsidian

Master Profile w Obsidian jako **single source of truth**:

- Skills, projekty, doświadczenie w jednym miejscu
- Agent czyta dane dynamicznie
- Aktualizacja profilu = lepsze CV

### 3. Pełny Tracing

Każda decyzja agenta jest tracewana:

- OpenAI Agents SDK tracing
- Integracja z Langfuse
- Możliwość debugowania "dlaczego agent wybrał ten skill?"

### 4. Polityka braku halucynacji

Agenci **nie wymyślają**:

- Skills tylko z listy kandydata
- Technologie projektów tylko z oryginalnych opisów
- Doświadczenie tylko z master-profile

---

## Co zrobiłem

1. Zaprojektowałem **architekturę multi-agent** z human-in-the-loop
2. Zaimplementowałem **Triage Agent** z Responses API
3. Zbudowałem **CV Tailor Agent** z OpenAI Agents SDK
4. Stworzyłem **Review Agent** do przygotowania do rozmów
5. Zintegrowałem z **Trello API** (karty, komentarze, załączniki)
6. Połączyłem z **Obsidian vault** jako źródłem prawdy
7. Zbudowałem **React frontend** do podglądu i konfiguracji CV
8. Wdrożyłem **PDF generation** z React PDF Renderer
9. Skonfigurowałem **tracing i observability** z Langfuse

---

## Umiejętności

<div class="skills-grid" markdown>

| Kategoria | Technologie |
|-----------|-------------|
| **AI/LLM** | OpenAI GPT-4o, OpenAI Agents SDK, RAG |
| **Backend** | Python, FastAPI, Pydantic, SQLite |
| **Frontend** | React, TypeScript, Next.js, Tailwind CSS |
| **Integracje** | Trello API, Obsidian, JustJoin.it |
| **DevOps** | Docker, Langfuse |

</div>

---

## Rezultaty

- ✅ Automatyzacja 80% procesu szukania pracy
- ✅ CV personalizowane w < 30 sekund
- ✅ Pełna kontrola nad procesem (human-in-the-loop)
- ✅ Tracing każdej decyzji agenta
- ✅ Zero halucynacji — tylko prawdziwe umiejętności
- ✅ Gotowe PDF z załącznikiem do Trello
