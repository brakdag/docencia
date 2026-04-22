# Work Order: Sanitization Group 2A - Individual Chapters (Part 1)

## Objective
Clean tokenization artifacts and ghost characters in the first half of the individual chapters.

## Target Files
- `capitulos/individual/01_gantt.tex`
- `capitulos/individual/02_idea.tex`
- `capitulos/individual/02_kanban.tex`
- `capitulos/individual/04_costos.tex`
- `capitulos/individual/05_costos_variables.tex`
- `capitulos/individual/06_estudio_mercado.tex`

## Protocol
For each file:
1. `read_file` $ightarrow$ 2. Clean in memory $ightarrow$ 3. `write_file`.

## QA
- Report the number of tokens cleaned per file.