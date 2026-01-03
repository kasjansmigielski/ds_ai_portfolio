# Analiza katastrofy promu Jan Heweliusz

*Projekt: listopad 2025*

**Rola:** Data Scientist

---

## Opis projektu

Katastrofa promu **MS Jan Heweliusz** (14 stycznia 1993 r.) przez lata była analizowana głównie w sposób opisowy, bez pełnej rekonstrukcji warunków meteorologicznych i ich wpływu na stateczność jednostki.

Celem projektu było **odtworzenie przebiegu katastrofy w sposób oparty na danych, fizyce i walidowalnych modelach**.

Przeprowadziłem **kompleksową analizę meteorologiczno-techniczną** łączącą:

- reanalizy meteorologiczne ERA5 (ECMWF),
- dane falowe CMEMS,
- prawa hydrodynamiki i stateczności,
- oficjalne raporty komisji i orzeczenia sądowe.

---

## Zakres analizy

### 1. Warunki meteorologiczne

- ciśnienie atmosferyczne (MSLP)
- prędkość i kierunek wiatru
- wysokość i energia fal
- analiza gradientu barycznego

### 2. Dynamika sztormu

- identyfikacja **explosive cyclogenesis** (kryterium Bergerona: ≥20 hPa / 24h)
- gwałtowna eskalacja warunków w godzinach poprzedzających katastrofę

### 3. Hydrodynamika i stateczność

- analiza fali bocznej (**Beam Sea**)
- mechanizm **parametric rolling**
- eskalacja przechyłów prowadząca do utraty stateczności

### 4. Walidacja danych

- porównanie ERA5 vs CMEMS
- korelacja, RMSE, bias
- ocena wiarygodności rekonstrukcji

---

## Kluczowe ustalenia

### Warunki pogodowe
- Spadek ciśnienia o **27 hPa w < 24h**
- Wiatr do **24.2 m/s (9°B – silny sztorm)**
- Energia fal wzrosła niemal **5× w ciągu 6 godzin**

### Hydrodynamika
- Fale uderzały w burtę pod kątem ~**60°**
- Maksymalna siła wiatru na burtę: **~393 kN**
- Jednostka pozostawała w strefie **Beam Sea**
- Rezonans przechyłów (parametric rolling)

### Eskalacja przechyłów
- 0° → 35° w 5h 40min
- 35° → 90° w **36 minut**

### Walidacja
- ERA5 vs CMEMS: **r = 0.982**
- R² = **0.964**
- Różnice w energii fal wynikają z nieliniowości (E ∝ H²), a nie z błędów danych

---

## Co zrobiłem

- Pozyskałem i przetworzyłem dane ERA5 i CMEMS
- Wykonałem analizy czasowe i przestrzenne
- Obliczyłem energię fal i siły działające na jednostkę
- Zbudowałem wizualizacje korelacji i eskalacji zjawisk
- Zestawiłem dane naukowe z ustaleniami komisji
- Opracowałem spójną narrację opartą na danych i fizyce

---

## Umiejętności

- Python
- Pandas
- NumPy
- xarray
- ERA5 (ECMWF)
- CMEMS (Copernicus Marine)
- Scientific Visualization
- Data Validation

---

## Rezultaty

- Ilościowa rekonstrukcja mechanizmu katastrofy
- Potwierdzenie zbieżności ekstremalnych zjawisk pogodowych i błędów techniczno-operacyjnych
- Wysoka wiarygodność analizy dzięki walidacji źródeł
- Przykład zastosowania Data Science do analizy zdarzeń historycznych

---

## Wnioski końcowe

Katastrofa MS *Jan Heweliusz* była **systemową kulminacją**:

- silnego sztormu (9°B),
- fali bocznej (Beam Sea),
- gwałtownej cyklogenezy,
- niewłaściwego przygotowania jednostki do rejsu.

Projekt pokazuje, jak **analiza danych, fizyka i walidacja modeli** pozwalają zrozumieć złożone zdarzenia w sposób obiektywny i replikowalny.

---

## Zdjęcia

![Analiza Beam Sea](../heweliusz/data/beam_sea_analysis.png)
![Energia i siła](../heweliusz/data/energy_and_force.png)
![Analiza wieloparametrowa](../heweliusz/data/multi_parameter_analysis.png)
![Przechył statku](../heweliusz/data/ship_heel.png)
![Warunki przestrzenne](../heweliusz/data/spatial_conditions.png)
![Róża wiatrowo-falowa](../heweliusz/data/wind_wave_rose.png)

