# Estymator Półmaratonu

*Data utworzenia: 2024-10-20*

## Opis projektu

Celem projektu było stworzenie aplikacji, która wykorzystując algorytm regresji do trenowania modeli, byłaby w stanie przewidzieć (na podstawie wcześniej wytrenowanych danych) czas, w jakim użytkownik przebiegnie półmaraton - poprzez podanie konkretnych danych.

## Główne funkcjonalności

- Umożliwienie użytkownikowi swobodnego wprowadzania danych (bez odpowiedniej konwersji zapisu) → wykorzystany model LLM ekstrahuje dane od użytkownika do struktury JSON i przygotowuje je do użycia przez model regresji
- Prosta funkcjonalność pozwala na ostateczną estymację czasu przebiegnięcia półmaratonu - przy użyciu wytrenowanego najlepszego modelu regresji
- Model LLM jest połączony z Langfuse do śledzenia cyklu życia modelu

## Trening modelu ML

Wykorzystałem narzędzia PyCaret i zawarłem implementację w notatniku gotowym do pobrania:

<a href="create_pipeline.ipynb" class="md-button md-button--primary">Pobierz Notebook: Trening modelu</a>

## Umiejętności

- Python
- PyCaret
- Machine Learning
- Langfuse
- OpenAI
- Streamlit
- Pandas
- Instructor
- Pydantic
- Dotenv

## Zdjęcia

![Tytuł](../halfmarathon_estimator/data/title.png)
![Wynik](../halfmarathon_estimator/data/result.png)

## Linki

[Link do repozytorium](https://github.com/kasjansmigielski/halfmarathon_estimator_app){ .md-button }

