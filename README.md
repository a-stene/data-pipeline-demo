# data-pipeline-demo

## Beskrivelse
Dette prosjektet henter aksjepriser fra Yahoo finance, renser og lagrer i strukturert format. 
Senere brukes det til å bygge og automatisere en maskinlæringspipeline (CI/CD og MLOps-prinsipper)

--- 
## funksjonalitet
- Henter data for en valgt ticker
- Lagrer i en dataframe
- Forbereder grunnlag for modelltrening og CI/CD-pipeline

## Teknologier
- Python 3.10+
- pandas
- yfinance 
- matplotlib

## Installasjon
### klon prosjektet
```bash
git clone https://github.com/a-stene/data-pipeline-demo.git
cd data-pipeline-demo
```

### Installer krav
```bash
pip install -r requirements.txt
```

## Hvordan kjøre
```bash
jupyter notebook data_pipeline.ipynb
```

## Forfatter
Prosjektet er del av en læringsplan for å bygge DevOps- og CI/CD-kompetanse i data science.