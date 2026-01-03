# Instrukcja uruchomienia i wdrożenia Portfolio

## 📋 Wymagania wstępne

- Conda (Anaconda/Miniconda/Mambaforge)
- Git

## 🚀 Uruchomienie lokalne

### 1. Klonowanie repozytorium (jeśli jeszcze nie masz)

```bash
git clone https://github.com/kasjansmigielski/ds_ai_portfolio.git
cd ds_ai_portfolio
```

### 2. Utworzenie środowiska Conda

```bash
conda env create -f environment.yml
conda activate ds_ai_portfolio
```

Lub jeśli środowisko już istnieje:

```bash
conda activate ds_ai_portfolio
```

### 3. Uruchomienie serwera deweloperskiego

```bash
mkdocs serve -a localhost:8003
```

Strona będzie dostępna pod adresem: **http://127.0.0.1:8003**

Serwer automatycznie przeładowuje stronę przy każdej zmianie plików.

### 4. Szybkie uruchomienie (jedna komenda)

```bash
conda activate ds_ai_portfolio && mkdocs serve -a localhost:8003
```

---

## 🌐 Deploy na GitHub Pages

### Metoda 1: Ręczny deploy (jednorazowa komenda)

```bash
mkdocs gh-deploy
```

Ta komenda:
- Buduje stronę do folderu `site/`
- Tworzy/aktualizuje branch `gh-pages`
- Pushuje na GitHub
- Strona będzie dostępna pod: https://kasjansmigielski.github.io/ds_ai_portfolio/

### Metoda 2: Automatyczny deploy przez GitHub Actions (zalecane)

Utwórz plik `.github/workflows/deploy.yml`:

```yaml
name: Deploy MkDocs to GitHub Pages

on:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
          
      - name: Install dependencies
        run: pip install mkdocs mkdocs-material
        
      - name: Deploy to GitHub Pages
        run: mkdocs gh-deploy --force
```

Po pushu na branch `main` strona automatycznie się zaktualizuje.

---

## 🔧 Konfiguracja GitHub Pages

1. Przejdź do repozytorium na GitHub
2. Settings → Pages
3. Source: **Deploy from a branch**
4. Branch: **gh-pages** / **(root)**
5. Zapisz

---

## 📁 Struktura projektu

```
ds_ai_portfolio/
├── docs/                    # Źródłowe pliki Markdown
│   ├── index.md            # Strona główna
│   ├── knowledge_seeker/   # Folder projektu
│   │   └── index.md
│   └── ...
├── mkdocs.yml              # Konfiguracja MkDocs
├── requirements.txt        # Zależności Python
└── INSTRUCTIONS.md         # Ta instrukcja
```

---

## 💡 Przydatne komendy

| Komenda | Opis |
|---------|------|
| `mkdocs serve` | Uruchom serwer deweloperski |
| `mkdocs build` | Zbuduj stronę do folderu `site/` |
| `mkdocs gh-deploy` | Deploy na GitHub Pages |
| `mkdocs new .` | Utwórz nowy projekt MkDocs |

---

## 🌐 Przełączanie języków (EN/PL)

Strona dostępna jest w dwóch wersjach językowych:

- **Angielska (domyślna):** `/ds_ai_portfolio/`
- **Polska:** `/ds_ai_portfolio/pl/`

Przełącznik języków znajduje się w headerze (ikona 🌐).

### Dodawanie tłumaczeń projektów

Polskie wersje projektów umieść w `docs/pl/{projekt}/index.md`.

Skrypt `scripts/sync_projects.py` automatycznie generuje wersje EN i PL z notatek Obsidian.

---

## 🐛 Rozwiązywanie problemów

### Port 8000 jest zajęty
```bash
mkdocs serve -a localhost:8080
```

### Brak modułu mkdocs
```bash
pip install mkdocs mkdocs-material
```

### Błędy przy deploy
Upewnij się, że masz uprawnienia do pushowania na repozytorium i że branch `gh-pages` nie jest chroniony.

