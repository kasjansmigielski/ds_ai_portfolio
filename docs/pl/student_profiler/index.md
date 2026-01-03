# Student Profiler

*Projekt: marzec 2025 — czerwiec 2025*

**Rola:** Backend / Data Engineer

**Firma:** GOTOIT sp. z o.o.

**Status:** Produkcja

---

## Opis projektu

Mentorzy i prowadzący kursy nie mieli narzędzia umożliwiającego systematyczne monitorowanie aktywności studentów na Discordzie.

Analiza zaangażowania, regularności pracy oraz historii interakcji:

- była rozproszona po wielu kanałach,
- wymagała ręcznego przeglądania wiadomości,
- nie dawała podstaw do automatycznych wniosków ani skalowania procesu mentoringu.

Brakowało jednego, centralnego systemu do zbierania i analizy danych.

Zaprojektowałem i rozwijam **Student Profiler** — narzędzie do automatycznego monitorowania aktywności studentów w środowisku Discord.

---

## Rozwiązanie

Rdzeniem systemu jest **Discord Bot**, który:

- pobiera dane historyczne z kanałów,
- nasłuchuje nowych wiadomości i zdarzeń w czasie rzeczywistym,
- zapisuje dane w relacyjnej bazie danych,
- zasila warstwę analityczną i interfejs użytkownika.

Architektura została przygotowana pod dalszy rozwój funkcji opartych o AI (humanizowany mentor bot, analiza sentymentu, OCR, modele predykcyjne).

---

## Architektura

![Architektura systemu](../student_profiler/data/architecture_logic.png)

---

## Główne funkcjonalności

- Integracja Discord Bot do monitorowania aktywności i automatycznego wysyłania wiadomości
- Cykliczne zbieranie danych z kanałów Discord (co godzinę)
- System przechowywania danych: PostgreSQL dla wiadomości, Digital Ocean Spaces dla załączników
- UI oparte na Streamlit do łatwego dostępu i analizy danych z Discorda
- Skalowalna architektura z planami implementacji funkcji AI

---

## Co zrobiłem

1. Zaprojektowałem architekturę systemu zgodnie z zasadami **Single Responsibility Principle**
2. Zaimplementowałem **Discord Bota** do:
   - pobierania historii wiadomości
   - nasłuchiwania nowych zdarzeń
   - obsługi automatycznych odpowiedzi
3. Stworzyłem mechanizm **cyklicznego zbierania danych (scheduler hourly)**
4. Zaprojektowałem i wdrożyłem bazę danych **PostgreSQL**
5. Zintegrowałem **DigitalOcean Spaces** do przechowywania załączników
6. Zbudowałem **UI analityczne w Streamlit** z wizualizacjami Plotly
7. Przygotowałem środowisko **Docker** do lokalnego i chmurowego uruchamiania
8. Zaimplementowałem konfigurację aplikacji z użyciem **pydantic-settings**

---

## Umiejętności

- Python
- Discord API
- PostgreSQL
- Streamlit
- Docker
- DigitalOcean
- Pandas
- SQL
- Plotly
- Psycopg
- Requests
- Schedule
- Pydantic-settings
- SRP design

---

## Rezultaty

- Centralne źródło danych o aktywności studentów na Discordzie
- Automatyczne i regularne zbieranie danych bez ręcznej ingerencji mentora
- Czytelny dashboard do analizy zaangażowania i trendów
- Stabilna baza pod dalszy rozwój funkcji AI:
  - analiza sentymentu komunikacji
  - predykcja spadku aktywności kursantów
  - humanizowany mentor bot

---

## Zdjęcia

![Przegląd dashboardu](../student_profiler/data/title.png)
![Wykres kołowy aktywności](../student_profiler/data/pie.png)
![Wykres pudełkowy aktywności](../student_profiler/data/box.png)

