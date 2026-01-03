# JustJoinIT Browser

*Start projektu: 2025-02-19*

## Opis projektu

JustJoinIT Browser to aplikacja Streamlit zaprojektowana do interaktywnego przeglądania najnowszych ofert pracy z platformy JustJoinIT. Projekt obejmował użycie biblioteki Requests do scrapowania danych o ofertach pracy, a następnie eksploracyjną analizę danych (EDA) w celu zrozumienia domeny i kategorii dostępnych na JustJoinIT. Dane zostały następnie przetworzone do odpowiedniego formatu CSV, który posłużył jako podstawa do budowy przyjaznego interfejsu użytkownika. Aplikacja wykorzystuje Geopandas do implementacji interaktywnej mapy polskich województw, umożliwiając intuicyjne filtrowanie ofert pracy na podstawie geolokalizacji. **W przyszłości aplikacja będzie rozwijana o algorytmy AI.**

## Główne funkcjonalności

- Niestandardowe przeglądanie ofert pracy IT z elastyczną konfiguracją interfejsu
- Interaktywna wizualizacja mapy do filtrowania geograficznego według regionów
- Wiele opcji filtrowania na podstawie technologii, poziomu doświadczenia i typu pracy
- Wizualizacja danych z wykresami i statystykami do lepszego zrozumienia rynku pracy
- Sortowanie i priorytetyzacja ofert pracy zdefiniowane przez użytkownika

## EDA

Przeprowadziłem szczegółową eksploracyjną analizę danych (EDA) używając Pandas do analizy danych, a także Plotly, Matplotlib i Seaborn do wizualizacji danych. Poniżej znajdziesz pliki dostępne do pobrania zawierające pełną analizę i zbiór danych:

<a href="job_offers_eda.ipynb" class="md-button md-button--primary">Pobierz Notebook: Analiza eksploracyjna</a>
<a href="job_offers_data.csv" class="md-button md-button--primary">Pobierz CSV: Oferty pracy</a>

## Umiejętności

- Python
- Requests
- Pandas
- Geopandas
- Shapely
- Folium
- Streamlit
- Plotly
- Pathlib
- EDA

## Zdjęcia

![Tytuł](../justjoinit_browser/data/title.png)
![Oferty](../justjoinit_browser/data/offers.png)
![Filtry](../justjoinit_browser/data/filters.png)
![Statystyki](../justjoinit_browser/data/statistics.png)
![Wizualizacje](../justjoinit_browser/data/visualizations.png)

