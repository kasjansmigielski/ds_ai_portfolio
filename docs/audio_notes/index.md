# Aplikacja: Audio Notes

*2024-10-03*

#### **Opis projektu:**
Celem projektu było stworzenie pierwszej aplikacji zasilanej AI. W tym celu wykorzystałem dwa modele LLM z firmy OpenAI: `whisper-1` (speech -> text) oraz `text-embeddings-3-large` (text -> embeddings). <br>
**Główne funkcjonalności:**<br>
- nagrywanie notatek głosowych oraz ich odsłuchiwanie,<br>
- tranksrypcja głosówek na tekst za pomocą AI,<br>
- możliwość gromadzenia notatek w bazie danych QDrant,<br>
- semantyczne wyszukiwanie danych, wykorzystujące algorytm przetwarzania tekstu na embeddings oraz znajdujące podobieństwa bazując na Cosinus Similarity.<br>

Aplikacja została wdrożona na Streamlit Community App i jest dostępna do publicznego użytku.

**Wykorzystane technologie:**<br>
- Python,<br>
- QDrant,<br>
- OpenAI embeddings,<br>
_ OpenAI whisper-1,<br>
- Streamlit,<br>
- Dotenv,<br>
- PyDub,<br>
- io,<br>
- md5.


![alt text](image.png)
![alt text](image-1.png)


**Link do repozytorium:** https://github.com/kasjansmigielski/audio_notes_app<br>
**Link do aplikacji:** https://audio-notes.streamlit.app/


[Przejdź do aplikacji](https://audio-notes.streamlit.app/){ .md-button }