---
# =============================================================================
# SZABLON NOTATKI PROJEKTU DLA OBSIDIAN (DWUJĘZYCZNY)
# =============================================================================
# Skopiuj ten plik do swojego Obsidian Vault (np. Vault/Projects/)
# i wypełnij danymi projektu.
#
# Ważne: Agent Cursor odczytuje TYLKO dane z tego frontmatter i sekcji poniżej.
# Nie wymyśla treści samodzielnie - to Ty kontrolujesz narrację!
# =============================================================================

id: nazwa-projektu                    # Wymagane: unikalne ID (bez spacji, małe litery)
title: "Project Name"                 # Wymagane: pełna nazwa (EN)
title_pl: "Nazwa Projektu"            # Nazwa po polsku
role: "AI/ML Engineer"                # Twoja rola w projekcie
status: completed                     # draft | in_progress | completed | production
featured: false                       # true = wyróżniony na stronie głównej
order: 10                             # Kolejność (niższe = wyżej na liście)

# Daty
date_from: "2025-01"                  # Format: YYYY-MM lub YYYY-MM-DD
date_to: "2025-06"                    # Puste jeśli w trakcie

# Tagi do filtrowania
tags:
  - machine-learning
  - python
  - nlp

# Stack technologiczny (do wyświetlenia na stronie)
stack:
  - Python
  - TensorFlow
  - FastAPI
  - Docker
  - AWS

# Linki zewnętrzne
repo: "https://github.com/username/project"
demo: "https://project-demo.com"

# Kluczowe osiągnięcia (EN)
highlights:
  - "Reduced processing time by 60%"
  - "Model achieved 95% accuracy on test set"
  - "System handles 10k requests/minute"

# Kluczowe osiągnięcia (PL)
highlights_pl:
  - "Zredukowałem czas przetwarzania o 60%"
  - "Model osiągnął 95% accuracy na zbiorze testowym"
  - "System obsługuje 10k requestów/minutę"

# Metryki liczbowe
metrics:
  accuracy: "95%"
  users: 2000
  requests_per_day: 50000
  latency_ms: 120

# =============================================================================
# ZDJĘCIA PROJEKTU
# =============================================================================
images:
  cover: "nazwa-projektu/cover.png"
  architecture: "nazwa-projektu/architecture.png"
  gallery:
    - path: "nazwa-projektu/screenshot1.png"
      caption: "User interface"
      caption_pl: "Interfejs użytkownika"
    - path: "nazwa-projektu/results.png"
      caption: "Experiment results"
      caption_pl: "Wyniki eksperymentów"

---

## Problem

Describe the business or technical problem you are solving.

- What was the context?
- Why was it important?
- What were the constraints?

## Problem_PL

Opisz problem biznesowy lub techniczny, który rozwiązujesz.

- Jaki był kontekst?
- Dlaczego to było ważne?
- Jakie były ograniczenia?

## Solution

Describe your approach and solution architecture.

- What strategy did you choose and why?
- What technologies did you use?
- What does the system architecture look like?

## Solution_PL

Opisz swoje podejście i architekturę rozwiązania.

- Jaką strategię wybrałeś i dlaczego?
- Jakie technologie użyłeś?
- Jak wygląda architektura systemu?

## What I did

Specific list of your actions and contributions.

1. Designed system architecture
2. Implemented ML pipeline
3. Conducted experiments with various models
4. Deployed solution to production
5. Configured monitoring and alerting

## What I did_PL

Konkretna lista Twoich działań i wkładu.

1. Zaprojektowałem architekturę systemu
2. Zaimplementowałem pipeline ML
3. Przeprowadziłem eksperymenty z różnymi modelami
4. Wdrożyłem rozwiązanie na produkcję
5. Skonfigurowałem monitoring i alerting

## Results

Measurable results and project impact.

- **Performance**: 60% faster processing
- **Quality**: 95% model accuracy
- **Business**: Saved 20h of work weekly
- **Scale**: System used by 2000+ users

## Results_PL

Mierzalne rezultaty i wpływ projektu.

- **Wydajność**: 60% szybsze przetwarzanie
- **Jakość**: 95% accuracy modelu
- **Biznes**: Oszczędność 20h pracy tygodniowo
- **Skala**: System używany przez 2000+ użytkowników
