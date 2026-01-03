# Larvixon-AI

*Start projektu: kwiecień 2025 — obecnie*

**Rola:** AI / Computer Vision Engineer

**Współpraca:** Uniwersytet Medyczny we Wrocławiu

---

## Opis projektu

**Larvixon-AI** to system oparty o **computer vision i deep learning**, który automatycznie analizuje zachowania ruchowe larw **Galleria mellonella** po iniekcji wybranych patogenów bakteryjnych.

Sepsa jest jednym z najpoważniejszych problemów współczesnej medycyny, a szybka identyfikacja patogenu ma kluczowe znaczenie dla wdrożenia odpowiedniej terapii. Klasyczne metody diagnostyczne:

- są czasochłonne (24–72 godziny),
- wymagają zaawansowanego zaplecza laboratoryjnego,
- nie zawsze pozwalają na szybkie podjęcie decyzji klinicznej.

Model **Galleria mellonella** umożliwia obserwację zmian behawioralnych po zakażeniu. Jednak dotychczasowa analiza była manualna, trudna do standaryzacji i ograniczona skalowalnością.

Projekt realizowany jest jako **praca magisterska** we współpracy z **Uniwersytetem Medycznym we Wrocławiu**.

---

## Jak to działa

Larvixon-AI to pipeline analizy wideo:

- **Video ingestion** — nagrania HD (25 FPS), różne warunki oświetleniowe
- **Warstwa Computer Vision** — detekcja obiektów (larw), segmentacja i maskowanie, śledzenie pozycji w kolejnych klatkach
- **Warstwa analizy** — obliczanie trajektorii, dystans, prędkość, kierunki, mapy ciepła aktywności
- **Dane i wizualizacje** — eksport CSV, analiza statystyczna, wizualizacje wyników

Architektura została przygotowana pod dalszą integrację z modelami deep learning.

---

## Co zrobiłem

1. Zaprojektowałem algorytm detekcji i śledzenia larw w wideo
2. Zaimplementowałem pipeline przetwarzania obrazu w OpenCV
3. Obsłużyłem różne warianty oświetlenia (góra / dół)
4. Wyznaczałem trajektorie i parametry kinematyczne ruchu
5. Przeprowadziłem analizę porównawczą grup:
   - kontrolnych
   - PBS
   - zakażonych *E. coli* (różne stężenia)
6. Zautomatyzowałem zapis danych i generowanie wizualizacji
7. Przeanalizowałem wyniki pod kątem różnic behawioralnych

---

## Umiejętności

- Python
- OpenCV
- Deep Learning
- Computer Vision
- NumPy
- Pandas
- Scientific Computing
- Video Processing

---

## Kluczowe rezultaty

- **100% skuteczności detekcji ruchu larw**
- Przetwarzanie nagrań wideo w czasie rzeczywistym (**25 FPS**)
- Istotne różnice pomiędzy grupami:
  - larwy kontrolne: ~5 mm/s
  - larwy zakażone: ~2.3 mm/s (wysokie stężenia)
- Wyraźne różnice w:
  - przebytych dystansach
  - rozkładzie przestrzennym aktywności
  - wzorcach ruchu

---

## Wpływ i przyszłe prace

Larvixon-AI stanowi podstawę do dalszych badań nad:

- automatyczną identyfikacją patogenów septycznych,
- przyspieszeniem diagnostyki zakażeń,
- wykorzystaniem deep learning w analizie behawioralnej.

Projekt łączy **AI engineering** z **badaniami biomedycznymi** i stanowi most pomiędzy nauką a praktycznymi zastosowaniami klinicznymi.

