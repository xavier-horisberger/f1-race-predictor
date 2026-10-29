# F1 Race Predictor

Progetto universitario di Machine Learning: previsione dei risultati di Formula 1 usando dati storici e modelli di classificazione/regressione.

> Stato: scaffolding iniziale. Il progetto non produce ancora previsioni e non contiene dati reali o modelli addestrati.

## Obiettivo

Costruire una pipeline end-to-end: raccolta dei dati, esplorazione, preprocessing, feature engineering senza data leakage, training, tuning, ensemble e valutazione. Un'osservazione del dataset ML rappresenterà un pilota iscritto a un GP. La prima sperimentazione sarà una classificazione binaria `is_podium`; in seguito potremo aggiungere la regressione di una posizione finale, gestendo separatamente i ritiri.

## Fonti previste

- [FastF1](https://docs.fastf1.dev/): sessioni, risultati, timing e dati moderni (quando disponibili).
- [Jolpica-F1](https://api.jolpi.ca/ergast/f1/): risultati e archivio storico.

Il periodo storico 1950-oggi è un obiettivo per l'archivio, non una garanzia di pari granularità delle feature.

## Struttura

```text
data/raw/                Download originali (non versionati)
data/processed/          Dati puliti (non versionati)
data/features/           Dataset per ML (non versionati)
notebooks/               Analisi e esperimenti, consegna del corso
src/collection/          Raccolta dati dalle API
src/processing/          Preprocessing e feature engineering
src/models/              Training, tuning e valutazione
src/prediction/          Generazione delle previsioni
models/                  Modelli addestrati (non versionati)
tests/                   Test automatici
docs/                    Note e schema dati
```

## Installazione (Windows PowerShell)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Avviare il primo notebook

```powershell
jupyter lab
```

Aprire `notebooks/01_data_exploration.ipynb`: esegue una verifica minima delle librerie, senza scaricare dati.

## Consegna ML

La consegna del corso richiede almeno **due modelli differenti visti a lezione**, preprocessing, train/test e/o cross-validation, tuning (`GridSearchCV` o `RandomizedSearchCV`), un ensemble/bagging, metriche e visualizzazioni, discussione dei risultati. Il codice (preferibilmente notebook) deve essere commentato. Non è richiesta una relazione scritta; è prevista presentazione in aula. La consegna formale è uno ZIP su iCorsi: **non basta il link GitHub**.

## Regole metodologiche

- Mai costruire una feature usando dati successivi all'istante della previsione.
- Tenere tutti i piloti dello stesso GP nello stesso segmento temporale (train/validation/test).
- Calcolare scaling, imputazione, encoding e tuning solo sui dati di training di ciascun fold.
- Conservare le previsioni prima della gara per una verifica successiva.
- Non committare cache, dataset pesanti, segreti o modelli binari.

## Collaborazione

Usare branch di feature, Pull Request e revisione reciproca prima del merge in `main`. Vedi `CONTRIBUTING.md`.
