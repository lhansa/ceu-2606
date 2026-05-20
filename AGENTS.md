# AGENTS.md

## Purpose

This file provides essential instructions and conventions for AI coding agents working in this project. It summarizes the project structure, build/test commands, and key patterns to ensure agents are immediately productive.

---

## Project Overview

- **Type:** Quarto slide project for CEU sessions (June 2026)
- **Main file:** [slides.qmd](slides.qmd) (Reveal.js slides, hidden Python code chunks)
- **Python helpers:** [src/](src/) contains code for monitoring and metrics recoding use cases
- **Data:** [data/raw/](data/raw/) for input Excel files, [data/processed/](data/processed/) for outputs
- **Config:** [_quarto.yml](_quarto.yml) for Quarto settings

## Build & Render

- Install dependencies: `pip install -r requirements.txt`
- Render slides: `quarto render slides.qmd`

## Key Conventions

- Python code is organized by use case: `monitoring.py` (data validation, time series), `metrics_recoding.py` (correlation, clustering)
- Data files are expected in Excel format in `data/raw/`
- Outputs are written to `data/processed/`
- All plotting uses Matplotlib
- Quarto code chunks use `echo: false` to hide code in slides

## Useful Links

- [README.md](README.md): Project structure, setup, and use cases

## Tips for Agents

- Prefer linking to documentation (README.md, slides.qmd) rather than duplicating content
- Follow the structure and naming conventions in `src/`
- For new helpers, add them to `src/` and document their purpose
- Use relative paths for data access
- If adding new use cases, update this file and the README

---

_Last updated: 2026-05-20_
