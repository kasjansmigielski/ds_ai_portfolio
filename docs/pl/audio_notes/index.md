# Audio Notes App

*Data utworzenia: 2024-10-03*

## Opis projektu

Celem projektu było stworzenie pierwszej aplikacji opartej o AI. W tym celu wykorzystałem dwa modele LLM od OpenAI: `whisper-1` (mowa -> tekst) i `text-embeddings-3-large` (tekst -> embeddingi).

## Główne funkcjonalności

- Nagrywanie i odsłuchiwanie notatek głosowych
- Transkrypcja głosu na tekst przy użyciu AI
- Możliwość zbierania notatek w bazie danych Qdrant
- Semantyczne wyszukiwanie danych przy użyciu algorytmu przetwarzania tekstu na embeddingi i znajdowania podobieństw na podstawie Cosinus Similarity

## Umiejętności

- Python
- Qdrant
- OpenAI embeddings
- OpenAI whisper-1
- Streamlit
- Dotenv
- PyDub
- io
- md5

## Zdjęcia

![Tytuł](../audio_notes/data/title.png)
![Wynik](../audio_notes/data/result.png)

## Wykorzystanie aplikacji

Aplikacja została wdrożona na Streamlit Community App i **pomaga mi łatwiej generować notatki, a co najważniejsze umożliwia kontekstowe wyszukiwanie przy użyciu AI.**

[Link do repozytorium](https://github.com/kasjansmigielski/audio_notes_app)


