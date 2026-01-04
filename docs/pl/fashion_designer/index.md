# Fashion Designer

*Data utworzenia: 2024-12-15*

## Opis projektu

Celem tego projektu było stworzenie imitacji projektanta mody. Pomysł na projekt przyszedł mi ze względu na potrzeby mojej partnerki życiowej, która projektuje bieliznę damską. Ta aplikacja ma zautomatyzować proces projektowania i dodatkowo będzie inspiracją do tworzenia nowych elementów ze świata mody.

## Architektura projektu

![Architektura](../fashion_designer/data/fashion_designer_architecture.png)

## Główne funkcjonalności

- Użytkownik wybiera, jaki typ bielizny chce zaprojektować
- Użytkownik określa początkową koncepcję projektu - następnie otrzymuje wizualną inspirację wygenerowaną przez AI
- Użytkownik podaje odpowiednie wymiary
- Aplikacja - wykorzystując odpowiednie wzory konstrukcyjne, oblicza i zapisuje parametry związane z konkretnym typem bielizny
- Następnie na podstawie parametrów obliczonych w poprzednim kroku tworzony jest rysunek konstrukcyjny, który jest wyświetlany w aplikacji
- Rysunek jest odpowiednio przygotowany do druku
- Użytkownik ma możliwość pobrania rysunku (całego lub podzielonego na części do druku)
- Na koniec model AI generuje rekomendacje związane z procesem tworzenia elementu zaprojektowanego przez użytkownika

## Umiejętności

- Python
- OpenAI
- Streamlit
- Matplotlib
- PIL
- Zipfile
- Requests

## Zdjęcia

![Tytuł](../fashion_designer/data/title.png)
![Przykładowy projekt 1](../fashion_designer/data/sample_design_1.png)
![Wymiary](../fashion_designer/data/dimension.png)
![Pełny rysunek](../fashion_designer/data/full_draw.png)
![Informacje o wymiarach](../fashion_designer/data/info_dimension.png)
![Rysunek A4](../fashion_designer/data/a4_draw.png)
![Rekomendacje 1](../fashion_designer/data/recommends_1.png)
![Rekomendacje 2](../fashion_designer/data/recommends_2.png)
![Przykładowy projekt 2](../fashion_designer/data/sample_design_2.png)
![Wymiary koszuli](../fashion_designer/data/shirt_dimension.png)
![Konstrukcja koszuli](../fashion_designer/data/shirt_construction.png)


