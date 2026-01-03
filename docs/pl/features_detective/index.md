# Features Detective App

*Data utworzenia: 2024-10-30*

## Opis projektu

Celem projektu było stworzenie uniwersalnej aplikacji pozwalającej na wykrywanie najważniejszych cech w danym zbiorze danych. W skrócie - użytkownik wgrywa dane lub ładuje gotowy zbiór danych w odpowiednim formacie, następnie wybiera automatyczną detekcję kolumny, którą chce analizować, lub dokonuje tego wyboru samodzielnie. Na koniec otrzymuje wygenerowany wykres istotności cech, które mają największy wpływ na wcześniej wybraną kolumnę. Użytkownik otrzymuje również czytelny opis wykresu wraz z rekomendacjami - co można poprawić, aby np. ulepszyć analizowane dane.

## Główne funkcjonalności

- Użytkownik może załadować plik CSV/JSON z danymi lub użyć gotowego przykładowego zbioru danych
- Użytkownik wskazuje kolumnę docelową → dodatkowo może skorzystać z automatycznej detekcji kolumny (generowanej przez LLM)
- Aplikacja automatycznie rozpoznaje, czy załadowane dane dotyczą problemu regresji czy klasyfikacji i na tej podstawie dobiera odpowiedni algorytm treningu modelu AI
- Na podstawie wytrenowanego modelu wyświetlany jest wykres zawierający najważniejsze cechy
- Na koniec użytkownik otrzymuje czytelny opis wykresu wraz z rekomendacjami - jakie działania wdrożyć, aby poprawić wyniki związane z analizowaną kolumną docelową

## Trening modelu ML

Wykorzystałem narzędzia PyCaret i zawarłem implementację w notatniku gotowym do pobrania:

<a href="model_training.ipynb" class="md-button md-button--primary">Pobierz Notebook: Trening modelu</a>

## Umiejętności

- Python
- Langfuse
- OpenAI
- Streamlit
- PyCaret (Classification & Regression)
- Pandas
- Matplotlib
- Instructor
- Pydantic
- Boto3

## Zdjęcia

![Tytuł](../features_detective/data/title.png)
![Wybór kolumny](../features_detective/data/choice_column.png)
![Rekomendacje](../features_detective/data/recommends.png)
![Wykres](../features_detective/data/plot.png)

## Linki

[Link do repozytorium](https://github.com/kasjansmigielski/feature_detective_app){ .md-button }

