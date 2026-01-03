# Quality Management System

*Projekt: czerwiec 2025 — październik 2025*

**Rola:** Data Scientist / Software Engineer

**Firma:** Agroment "ZEHS" Lubań

**Status:** Produkcja



---

## Opis projektu

W organizacjach przemysłowych dane jakościowe i techniczne są często **rozproszone pomiędzy wieloma źródłami**:

- raporty jakości w Excelu,
- dokumentacja techniczna w PDF,
- instrukcje procesowe w różnych lokalizacjach,
- historia działań korygujących w osobnych plikach.

W efekcie:

- znalezienie właściwego dokumentu zajmuje zbyt dużo czasu,
- dane są niespójne i trudne do porównania,
- brak jednego miejsca do analizy jakości i decyzji,
- wiedza organizacyjna jest silnie zależna od konkretnych osób.

Zaprojektowałem **Quality Management System (QMS)**, którego głównym celem było stworzenie **jednego, centralnego źródła prawdy** dla danych jakościowych i wiedzy technicznej.

---

## Rozwiązanie

System łączy:

- klasyczny QMS (raporty, działania, metryki),
- warstwę **Knowledge Management**,
- **semantic search** umożliwiający wyszukiwanie w języku naturalnym.

Całość została udostępniona jako **aplikacja Streamlit** pełniąca rolę operacyjnego dashboardu jakości.

---

## Architektura

QMS został zaprojektowany jako system integrujący wiele źródeł danych:

- **Data ingestion** — import danych z plików PDF i Excel, normalizacja i standaryzacja
- **Centralna baza danych** — relacyjna baza jako single source of truth, ujednolicone modele danych jakościowych
- **Warstwa wiedzy** — ekstrakcja treści dokumentów, embeddingi i indeks semantyczny
- **Warstwa aplikacyjna** — Streamlit jako interfejs użytkownika, dashboardy, raporty, wyszukiwanie

Architektura została zaprojektowana z myślą o:

- integracji z systemami ERP / CRM,
- przyszłym rozszerzeniu o kolejne moduły AI.

---

## Kluczowe funkcje

### Inteligentne wyszukiwanie semantyczne

- wyszukiwanie rysunków, instrukcji i raportów
- zapytania w języku naturalnym
- brak potrzeby znajomości struktury folderów

### Scentralizowane i ustandaryzowane dane

- wszystkie dane jakościowe w jednym miejscu
- spójne formaty i aktualne wersje dokumentów
- eliminacja duplikatów i nieaktualnych plików

### Automatyczne raportowanie i analityka

- dashboardy jakościowe
- statusy działań korygujących
- szybki przegląd KPI jakości

### Architektura gotowa na integrację

- przygotowanie pod integrację z ERP / CRM
- modularna struktura danych
- gotowość pod dalsze systemy AI

---

## Co zrobiłem

1. Przeanalizowałem istniejące źródła danych jakościowych
2. Zaprojektowałem ujednolicony model danych
3. Zaimplementowałem import i transformację danych z PDF i Excel
4. Stworzyłem centralną bazę danych jako single source of truth
5. Zbudowałem warstwę semantic search nad dokumentacją
6. Opracowałem dashboard jakości w Streamlit
7. Zautomatyzowałem raportowanie i monitoring działań
8. Przygotowałem architekturę pod przyszłe integracje i AI

---

## Umiejętności

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

## Rezultaty

- Redukcja czasu wyszukiwania dokumentów nawet o **70%**
- Jedno, spójne źródło danych jakościowych
- Lepsza przejrzystość procesów i historii działań
- Szybsze podejmowanie decyzji jakościowych
- Usprawniona współpraca między:
  - produkcją
  - jakością
  - zakupami
- Solidna baza pod dalszy rozwój systemów AI w organizacji

