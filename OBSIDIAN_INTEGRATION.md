# 🔗 Integracja Portfolio z Obsidian

Ten dokument opisuje jak skonfigurować automatyczną synchronizację projektów z Obsidian do portfolio.

## 📋 Spis treści

1. [Architektura](#architektura)
2. [Konfiguracja Obsidian](#konfiguracja-obsidian)
3. [Konfiguracja MCP w Cursor](#konfiguracja-mcp-w-cursor)
4. [Użycie skryptu synchronizacji](#użycie-skryptu-synchronizacji)
5. [Workflow agenta](#workflow-agenta)

---

## 🏗️ Architektura

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│                 │     │                  │     │                 │
│    OBSIDIAN     │────▶│  CURSOR + MCP    │────▶│   PORTFOLIO     │
│    (Vault)      │     │  (Agent AI)      │     │   (GitHub)      │
│                 │     │                  │     │                 │
└─────────────────┘     └──────────────────┘     └─────────────────┘
        │                       │                       │
    Notatki MD              Parsowanie              MkDocs Site
    z frontmatter          + walidacja             GitHub Pages
```

**Zasady bezpieczeństwa:**
- Agent CZYTA z Obsidian (nie modyfikuje)
- Agent ZAPISUJE do repozytorium portfolio
- Publikacja wymaga Twojego review (PR lub manualny push)

---

## 📓 Konfiguracja Obsidian

### 1. Utwórz folder na projekty

W swoim Obsidian Vault stwórz dedykowany folder:

```
Vault/
├── Projects/           ◀── Tutaj notatki o projektach
│   ├── knowledge-seeker.md
│   ├── student-profiler.md
│   └── audio-notes.md
├── Daily Notes/
└── ...
```

### 2. Użyj szablonu

Skopiuj szablon z `scripts/project_template.md` do Obsidian jako template.

**Ważne sekcje frontmatter:**

```yaml
---
id: knowledge-seeker        # Unikalne ID (folder w docs/)
title: "Knowledge Seeker"   # Nazwa wyświetlana
status: production          # draft | in_progress | completed | production
featured: true              # Wyróżniony na stronie głównej
tags: [rag, llm, python]    # Tagi do filtrowania
stack: [Python, Qdrant]     # Stack technologiczny
highlights:                 # Kluczowe osiągnięcia
  - "RAG over 400+ videos"

# Zdjęcia projektu (automatycznie kopiowane do portfolio)
images:
  cover: "knowledge-seeker/cover.png"           # Zdjęcie główne
  architecture: "knowledge-seeker/arch.png"     # Diagram architektury
  gallery:                                      # Galeria screenshotów
    - path: "knowledge-seeker/ui.png"
      caption: "Interfejs użytkownika"
    - path: "knowledge-seeker/results.png"
      caption: "Wyniki wyszukiwania"
---
```

**Ważne sekcje markdown:**

- `## Problem` — opisz problem biznesowy
- `## Solution` — Twoje podejście
- `## What I did` — konkretne działania
- `## Results` — mierzalne rezultaty

### 3. Struktura zdjęć w Obsidian

Zdjęcia powinny być w podfolderze o nazwie takiej jak `id` projektu:

```
Vault/Projects/
├── knowledge-seeker.md           <- notatka projektu
├── knowledge-seeker/             <- folder ze zdjęciami
│   ├── cover.png                 <- zdjęcie główne
│   ├── architecture.png          <- diagram architektury
│   ├── screenshot1.png           <- screenshoty
│   └── results.png               <- wykresy
├── student-profiler.md
└── student-profiler/
    ├── cover.png
    └── dashboard.png
```

### 4. Przykładowa notatka

```markdown
---
id: knowledge-seeker
title: "Knowledge Seeker"
role: "AI/ML Engineer"
status: production
featured: true
tags: [rag, qdrant, embeddings, llm, streamlit]
date_from: 2025-03
date_to: 2025-08
stack: [Python, OpenAI, Qdrant, Streamlit, Docker]
repo: https://github.com/kasjansmigielski/knowledge-seeker
demo: https://knowledge-seeker.streamlit.app
highlights:
  - RAG over 400+ videos
  - Monitoring with Langfuse
  - 2000+ aktywnych użytkowników
metrics:
  users: 2000
  videos_indexed: 400
  avg_response_time_ms: 850

# Zdjęcia (ścieżki względne do folderu Projects/)
images:
  cover: "knowledge-seeker/cover.png"
  architecture: "knowledge-seeker/architecture.png"
  gallery:
    - path: "knowledge-seeker/ui-main.png"
      caption: "Główny interfejs wyszukiwania"
    - path: "knowledge-seeker/ui-results.png"
      caption: "Wyniki z timestampami"
    - path: "knowledge-seeker/langfuse.png"
      caption: "Dashboard monitoringu Langfuse"
---

## Problem

Użytkownicy platformy edukacyjnej mieli trudności z odnalezieniem 
konkretnych informacji w 400+ nagraniach wideo. Manualne przeszukiwanie 
zajmowało średnio 15 minut na pytanie.

## Solution

Zaprojektowałem system RAG (Retrieval-Augmented Generation), który:
- Transkrybuje wideo na tekst
- Indeksuje treści w bazie wektorowej Qdrant
- Odpowiada na pytania w języku naturalnym

## What I did

1. Zbudowałem pipeline transkrypcji z Whisper
2. Zaimplementowałem chunking i embedding dokumentów
3. Skonfigurowałem Qdrant jako vector store
4. Stworzył frontend w Streamlit
5. Dodałem monitoring z Langfuse

## Results

- **Czas wyszukiwania**: z 15 min → 30 sekund
- **Satysfakcja użytkowników**: 4.8/5
- **Skala**: 2000+ aktywnych użytkowników
```

---

## ⚙️ Konfiguracja MCP w Cursor

### 1. Zainstaluj MCP filesystem server

Dodaj do konfiguracji Cursor (`~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "obsidian-vault": {
      "command": "npx",
      "args": [
        "-y",
        "@anthropics/mcp-filesystem",
        "/Users/kasjansmigielski/Obsidian/Vault"
      ]
    }
  }
}
```

**Uwaga:** Zmień ścieżkę `/Users/kasjansmigielski/Obsidian/Vault` na swoją.

### 2. Operacje dostępne dla agenta

Po konfiguracji MCP, agent Cursor może:

| Operacja | Opis |
|----------|------|
| `list_directory` | Lista plików w vault |
| `read_file` | Odczyt notatki projektu |
| `search_files` | Wyszukiwanie w vault |

Agent NIE może modyfikować Twojego vault — tylko czytać.

---

## 🔄 Użycie skryptu synchronizacji

### Ręczna synchronizacja

```bash
# Pełna synchronizacja
python scripts/sync_projects.py \
  --vault-path ~/Obsidian/Vault/Projects \
  --output-path docs

# Tryb testowy (dry run)
python scripts/sync_projects.py \
  --vault-path ~/Obsidian/Vault/Projects \
  --dry-run
```

### Co robi skrypt:

1. ✅ Czyta wszystkie `.md` z folderu Projects
2. ✅ Parsuje frontmatter YAML
3. ✅ Waliduje wymagane pola
4. ✅ **Kopiuje zdjęcia** z vault do `docs/{projekt}/images/`
5. ✅ Generuje strony MkDocs w `docs/`
6. ✅ Tworzy `data/projects.json` z metadanymi
7. ✅ Zapisuje log synchronizacji

### Output

```
📂 Znaleziono 5 plików projektów

📄 Przetwarzam: knowledge-seeker.md
      📷 Skopiowano: cover.png
      📷 Skopiowano: architecture.png
      📷 Skopiowano: ui-main.png
      📷 Skopiowano: ui-results.png
   ✅ Zsynchronizowano: Knowledge Seeker

📄 Przetwarzam: student-profiler.md
      📷 Skopiowano: cover.png
   ✅ Zsynchronizowano: Student Profiler

==================================================
📋 PODSUMOWANIE SYNCHRONIZACJI
==================================================
✅ Zsynchronizowano: 5
📷 Skopiowano zdjęć: 12
❌ Błędy: 0
⏭️  Pominięto: 0
```

---

## 🤖 Workflow agenta

### Jak rozmawiać z Cursor:

```
"Zsynchronizuj projekty z mojego Obsidiana i zaktualizuj portfolio"
```

Agent wykona:
1. Odczyta pliki z `Vault/Projects/`
2. Sparsuje frontmatter i sekcje
3. Wygeneruje/zaktualizuje pliki w `docs/`
4. Przygotuje commit z changelogiem

### Bezpieczna procedura publikacji

**Opcja A: Review przed commitem**
```
"Pokaż mi zmiany przed commitem"
```

**Opcja B: PR zamiast bezpośredniego push**
```
"Stwórz branch feature/update-projects i zrób PR"
```

**Opcja C: Ty robisz push**
```bash
# Agent robi commit, Ty robisz push
git push origin main
```

---

## 🛡️ Jak unikać "AI slop"

### Problem: Agent może tworzyć generyczną treść

**Rozwiązanie:** Agent używa TYLKO danych z Twojego frontmatter i sekcji:

| Źródło | Co agent robi |
|--------|---------------|
| `title` | Nagłówek strony |
| `highlights` | Lista osiągnięć |
| `## Problem` | Sekcja "Problem" |
| `## Results` | Sekcja "Rezultaty" |

Agent NIE wymyśla treści — tylko formatuje Twoje dane.

### Walidacja przed publikacją

```bash
# Sprawdź wygenerowane pliki
mkdocs serve

# Przejrzyj diff
git diff docs/
```

---

## 📊 Struktura data/projects.json

Po synchronizacji powstaje plik z metadanymi:

```json
[
  {
    "id": "knowledge-seeker",
    "title": "Knowledge Seeker",
    "status": "production",
    "featured": true,
    "tags": ["rag", "qdrant", "llm"],
    "stack": ["Python", "OpenAI", "Qdrant"],
    "highlights": ["RAG over 400+ videos"],
    "metrics": {"users": 2000}
  }
]
```

Możesz użyć tego pliku do:
- Dynamicznego generowania strony głównej
- Filtrowania projektów po tagach
- Tworzenia sekcji "Featured projects"

---

## 🚀 Quick Start

1. **Stwórz 3 projekty w Obsidian** używając szablonu
2. **Uruchom synchronizację:**
   ```bash
   python scripts/sync_projects.py --vault-path ~/Obsidian/Vault/Projects --dry-run
   ```
3. **Sprawdź preview:**
   ```bash
   mkdocs serve
   ```
4. **Deploy:**
   ```bash
   git add . && git commit -m "Sync projects from Obsidian"
   git push origin main
   ```

