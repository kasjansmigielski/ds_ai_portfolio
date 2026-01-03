# Predykcja ceny Bitcoina

*Data utworzenia: 2025-02-04*

## Opis projektu

Ten projekt koncentruje się na rozwoju modelu predykcyjnego dla ruchów cen Bitcoina przy użyciu **technik deep learning**. Podejście integruje kompleksową **Eksploracyjną Analizę Danych (EDA)** z zaawansowanymi metodami prognozowania szeregów czasowych, w szczególności **sieciami neuronowymi Long Short-Term Memory (LSTM)**. Wykorzystując historyczne dane cenowe Bitcoina (z Kaggle), wskaźniki techniczne i metryki sentymentu rynkowego, model ma na celu prognozowanie przyszłych trendów cenowych ze znaczącą dokładnością. Implementacja wykorzystuje frameworki **TensorFlow** i **Keras** do budowy, trenowania i ewaluacji architektury LSTM, która jest szczególnie odpowiednia do wychwytywania zależności czasowych w finansowych szeregach czasowych. Projekt demonstruje zastosowanie deep learning do analizy rynku kryptowalut i dostarcza wglądu w czynniki wpływające na zmienność cen Bitcoina.

## Główne funkcjonalności

- Kompleksowa Eksploracyjna Analiza Danych (EDA) historycznych danych cenowych Bitcoina i powiązanych metryk rynkowych
- Preprocessing danych wraz z technikami normalizacji do optymalizacji wydajności modelu
- Implementacja feature engineering do ekstrakcji znaczących predyktorów z surowych danych rynkowych
- Rozwój architektury sieci neuronowej LSTM (Long Short-Term Memory) do prognozowania szeregów czasowych
- Integracja frameworków TensorFlow i Keras do budowy, trenowania i ewaluacji modelu
- Dostrajanie hiperparametrów w celu optymalizacji dokładności i zdolności generalizacji modelu
- Wizualizacja przewidywanych vs rzeczywistych ruchów cen do oceny wydajności modelu
- Analiza błędów predykcji w celu identyfikacji warunków rynkowych wpływających na dokładność prognozy

## Umiejętności

- Python
- Pandas
- EDA
- NumPy
- Scikit-learn
- TensorFlow
- Keras
- LSTM
- Matplotlib
- LaTeX

## Raport projektu

**Możesz pobrać** i przejrzeć kompletny raport projektu ze szczegółową metodologią i wynikami tutaj: <a href="/ds_ai_portfolio/bitcoin_prediction/Bitcoin_Prediction_Report.pdf" target="_blank">Raport predykcji ceny Bitcoina</a>

## Zdjęcia

![Macierz korelacji](/ds_ai_portfolio/bitcoin_prediction/data/corr_mat.png)
![Wartości odstające](/ds_ai_portfolio/bitcoin_prediction/data/outliers.png)
![Normalizacja](/ds_ai_portfolio/bitcoin_prediction/data/normalization.png)
![Architektura LSTM](/ds_ai_portfolio/bitcoin_prediction/data/lstm_architecture.png)
![Trening](/ds_ai_portfolio/bitcoin_prediction/data/training.png)
![Wynik](/ds_ai_portfolio/bitcoin_prediction/data/result.png)
