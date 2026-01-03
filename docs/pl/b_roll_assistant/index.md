# B-roll Assistant

*Start projektu: listopad 2025 — obecnie*

**Rola:** AI / Backend Engineer

---

## Opis projektu

**B-roll Assistant** to inteligentny asystent AI, który **automatycznie kataloguje materiały wideo** i umożliwia ich **natychmiastowe wyszukiwanie**.

W newsroomach i środowiskach produkcji wideo czas jest kluczowy. Redaktorzy i montażyści muszą **błyskawicznie znaleźć odpowiedni B-roll**, często pod presją deadline'ów. W praktyce:

- materiały wideo są słabo opisane lub wcale,
- nazwy plików są niejednoznaczne,
- ręczne tagowanie jest kosztowne i nierealne,
- klasyczne wyszukiwanie po folderach nie skaluje się.

System:

- analizuje wideo bez ingerencji użytkownika,
- generuje snapshoty i opisy ujęć przy użyciu AI,
- łączy wyszukiwanie klasyczne z **semantic search**,
- uczy się na podstawie ocen redaktorów.

Dzięki temu redaktor nie musi wiedzieć *jak nazwano plik* — wystarczy opisać **to, czego szuka**.

---

## Jak to działa

### 1. Smart Catalog Setup

- System adaptuje się do istniejącej struktury plików
- Nie wymaga ręcznego porządkowania materiałów
- Obsługuje duże archiwa B-roll

### 2. AI Shot Descriptions

- Automatyczne generowanie snapshotów (FFmpeg)
- Analiza wizualna ujęć (AI Vision)
- Opisy tekstowe dla każdego klipu: obiekty, sceny, kontekst, atmosfera
- Każdy klip otrzymuje **bogaty opis semantyczny** bez ręcznego tagowania

### 3. Dual Search & Continuous Learning

- **Keyword search** (szybkie, precyzyjne zapytania)
- **Semantic search** (wyszukiwanie po znaczeniu i koncepcjach)

Przykłady zapytań:

- "szkło"
- "przezroczysty pojemnik"
- "napięty wiec polityczny"
- "tłum nerwowo czekający"

System umożliwia ocenę wyników, co:

- poprawia trafność,
- dostosowuje ranking,
- zwiększa skuteczność wyszukiwania w czasie.

---

## Architektura

B-roll Assistant to **multimodalny pipeline**:

- **Video ingestion** — analiza struktury plików, ekstrakcja klatek
- **AI processing** — vision → opis obrazu, tekst → embeddingi
- **Search layer** — klasyczne indeksy, wektorowa baza danych
- **Feedback loop** — oceny użytkowników, korekta rankingu wyników

Zaprojektowany pod **wydajność i skalowanie** w środowiskach medialnych.

---

## Co zrobiłem

1. Zaprojektowałem architekturę systemu do analizy B-roll
2. Zaimplementowałem pipeline ekstrakcji klatek wideo
3. Zintegrowałem AI Vision do analizy ujęć
4. Stworzyłem system automatycznych opisów klipów
5. Zbudowałem **dual search engine** (keyword + semantic)
6. Wdrożyłem wyszukiwanie oparte o embeddingi
7. Zaprojektowałem mechanizm feedbacku użytkowników
8. Przygotowałem backend API i strukturę danych
9. Opakowałem system w środowisko kontenerowe (Docker)

---

## Umiejętności

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

## Rezultaty

- Odnalezienie właściwego B-roll w **sekundy zamiast minut**
- Brak potrzeby ręcznego tagowania materiałów
- Lepsze wykorzystanie istniejących archiwów wideo
- System, który **uczy się razem z zespołem redakcyjnym**
- Solidna baza pod: newsroomy, media houses, platformy contentowe

---

## Zdjęcia

![Wyszukiwanie murawa](/ds_ai_portfolio/b_roll_assistant/data/murawa.png)
![Wyszukiwanie zabytki](/ds_ai_portfolio/b_roll_assistant/data/zabytki.png)
![Zarządzanie plikami](/ds_ai_portfolio/b_roll_assistant/data/file_management.png)
![Ujęcia z drona](/ds_ai_portfolio/b_roll_assistant/data/dron.png)
![Pisanie](/ds_ai_portfolio/b_roll_assistant/data/pisanie.png)

