# ceu-2606

Quarto slide project for CEU sessions in June 2026.

## Project structure

- `slides.qmd`: revealjs slides with hidden Python code chunks (`echo: false`).
- `src/`: Python helpers for the two use cases.
- `data/raw/`: local input files (Excel).
- `data/processed/`: generated outputs.
- `_quarto.yml`: Quarto project and execution defaults.

## Planned use cases

1. Monitoring data (time series plotting)
2. Recoding metrics (correlation + hierarchical clustering/dendrogram)

## Local setup

```bash
pip install -r requirements.txt
quarto render slides.qmd
```
