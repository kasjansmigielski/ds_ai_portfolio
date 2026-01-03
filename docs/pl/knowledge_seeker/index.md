# Knowledge Seeker

*Start projektu: kwiecień 2025 — sierpień 2025*

**Rola:** Tech Lead / Architekt

**Firma:** GOTOIT sp. z o.o.

**Status:** Produkcja

---

## Opis projektu

**Knowledge Seeker** to zaawansowane narzędzie do transkrypcji, indeksowania i wyszukiwania informacji w nagraniach wideo.

Użytkownicy posiadający dostęp do dużych zasobów nagrań wideo (kursy, szkolenia, sesje mentoringowe) mieli trudności z szybkim odnajdywaniem konkretnych informacji. Manualne przeszukiwanie setek materiałów było czasochłonne i nieefektywne.

**Jako lider projektu** koordynuję rozwój systemu wykorzystującego najnowsze technologie AI do przetwarzania mowy na tekst i implementacji zaawansowanych mechanizmów wyszukiwania semantycznego.

Aplikacja umożliwia użytkownikom nie tylko znajdowanie konkretnych informacji w obszernych zasobach wideo, ale także generowanie odpowiedzi na zapytania w oparciu o zgromadzoną wiedzę przy użyciu architektury **RAG (Retrieval-Augmented Generation)**.

---

## Rozwiązanie

Zaprojektowałem system oparty o architekturę **RAG (Retrieval-Augmented Generation)**, łączący automatyczną transkrypcję nagrań wideo, wyszukiwanie semantyczne w bazie wektorowej oraz generowanie odpowiedzi przez modele językowe.

---

## Architektura

![Architektura systemu](../knowledge_seeker/data/architecture.png)

---

## Główne funkcjonalności

- Transkrypcja nagrań wideo na tekst z zachowaniem metadanych czasowych (timestampy)
- Przetwarzanie transkrypcji poprzez chunking i generowanie embeddingów
- Baza wektorowa do przechowywania i efektywnego wyszukiwania embeddingów
- Interfejs użytkownika umożliwiający zarówno proste, jak i semantyczne wyszukiwanie treści
- System RAG (Retrieval-Augmented Generation) do generowania odpowiedzi na zapytania użytkowników
- Wdrożenie w chmurze Digital Ocean zapewniające skalowalność i dostępność
- Eksport danych w formatach JSON i możliwość streamingu do API użytkownika

---

## Co zrobiłem

1. Zaprojektowałem architekturę systemu oraz pipeline przetwarzania danych
2. Zaimplementowałem transkrypcję audio → tekst z użyciem Whisper
3. Opracowałem chunking dokumentów oraz generowanie embeddingów
4. Skonfigurowałem bazę wektorową Qdrant
5. Zbudowałem backend API w FastAPI
6. Stworzyłem interfejs użytkownika w Streamlit
7. Wdrożyłem system w chmurze DigitalOcean (Docker)

---

## Plan rozwoju

- Integracja z dodatkowymi źródłami danych (dokumenty, prezentacje, audio)
- Rozbudowa mechanizmów RAG o zaawansowane techniki filtrowania i re-rankingu
- Implementacja komponentów do automatycznej weryfikacji i aktualizacji bazy wiedzy
- Optymalizacja procesów indeksowania i wyszukiwania dla większych zbiorów danych
- Rozwój interfejsu API umożliwiającego integrację z zewnętrznymi aplikacjami

---

## Umiejętności

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

## Rezultaty

- **400+ nagrań wideo** przeszukiwalnych w czasie rzeczywistym
- Skrócenie czasu odnajdywania informacji z **minut do sekund**
- Gotowy do skalowania, produkcyjny system AI

