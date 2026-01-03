# Find Friends App

*Data utworzenia: 2024-10-09*

## Opis projektu

Celem projektu było stworzenie aplikacji, która umożliwiałaby wykorzystanie modelu klastrowania do dopasowania użytkownika do odpowiedniej grupy z załadowanego zbioru danych (dane pochodzą z anonimowej ankiety) - na podstawie danych podanych przez użytkownika.

## Główne funkcjonalności

- Użytkownik filtruje podstawowe dane, takie jak: wiek, wykształcenie, płeć, ulubione zwierzęta lub ulubione miejsca - odpowiadające jego preferencjom
- Następnie wcześniej wytrenowany model klastrowania tworzy odpowiednią liczbę klastrów dla danych ankietowych i dopasowuje preferencje użytkownika do pasującej grupy
- Na koniec, przy użyciu LLM, generowane są odpowiednie opisy klastrów

## Trening modelu ML

Wykorzystałem narzędzia Scikit-learn i zawarłem implementację w notatniku gotowym do pobrania:

<a href="clustering_model_training.ipynb" class="md-button md-button--primary">Pobierz Notebook: Trening modelu</a>

## Nazewnictwo klastrów

Wykorzystałem model LLM i zawarłem implementację w notatniku gotowym do pobrania:

<a href="clusters_naming.ipynb" class="md-button md-button--primary">Pobierz Notebook: Nazewnictwo klastrów</a>

## Umiejętności

- Python
- Langfuse
- OpenAI
- Streamlit
- Scikit-learn
- Plotly
- PyCaret (Clustering)
- NumPy
- Matplotlib

## Zdjęcia

![Pierwszy widok](../find_friends/data/first.png)
![Drugi widok](../find_friends/data/second.png)

## Linki

[Link do repozytorium](https://github.com/kasjansmigielski/find_friends_app){ .md-button }

