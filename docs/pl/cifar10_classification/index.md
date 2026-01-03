# Klasyfikacja obrazów CIFAR-10

*Start projektu: 2025-02-07*

## Opis projektu

Ten projekt implementuje zaawansowaną architekturę **Konwolucyjnej Sieci Neuronowej (CNN)** do klasyfikacji obrazów przy użyciu zbioru danych **CIFAR-10**. Badanie koncentruje się na rozwoju i optymalizacji modelu deep learning zdolnego do dokładnej klasyfikacji obrazów w 10 różnych kategoriach. Poprzez systematyczne eksperymenty z różnymi architekturami sieci, **technikami augmentacji danych** i **optymalizacją hiperparametrów**, projekt demonstruje jak zbudować solidny system **Computer Vision**. Implementacja wykorzystuje frameworki **TensorFlow** i **Keras**, stosując najlepsze praktyki w projektowaniu CNN, w tym warstwy konwolucyjne, operacje pooling, batch normalization i regularyzację dropout. Projekt podkreśla znaczenie strategii **cross-validation** i metryk ewaluacji modelu do tworzenia uogólnialnego modelu klasyfikacji z wysoką dokładnością na niewidzianych danych.

## Główne funkcjonalności

- Implementacja niestandardowych architektur CNN do zadań klasyfikacji obrazów
- Zastosowanie technik augmentacji danych w celu zwiększenia odporności modelu i zapobiegania overfittingowi
- Optymalizacja hiperparametrów przy użyciu **RandomSearch** do identyfikacji optymalnych konfiguracji modelu
- Implementacja **K-Fold** cross-validation dla zapewnienia wiarygodnej ewaluacji modelu
- Wykorzystanie **early stopping** i planowania **learning rate** dla poprawy efektywności treningu
- Kompleksowa ewaluacja modelu przy użyciu **macierzy pomyłek, precision, recall** i **F1-score**
- Wizualizacja wydajności modelu, map cech i wyników klasyfikacji
- Analiza porównawcza różnych architektur modeli i ich metryk wydajności

## Umiejętności

- Python
- TensorFlow
- Keras
- Augmentation
- CNN
- RandomSearch
- Scikit-learn
- NumPy
- KFold
- LaTeX

## Raport projektu

**Możesz pobrać** i przejrzeć kompletny raport projektu ze szczegółową metodologią i wynikami tutaj: [Raport klasyfikacji obrazów CIFAR-10](CV_Project.pdf)

## Zdjęcia

![Augmentacja](../cifar10_classification/data/augmentation.png)
![Klasy](../cifar10_classification/data/classes.png)
![Obrazy](../cifar10_classification/data/pictures.png)
![Odchylenie standardowe](../cifar10_classification/data/st_dev.png)
![Trening](../cifar10_classification/data/training.png)
![Macierz](../cifar10_classification/data/matrix.png)

