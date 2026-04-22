# Work Order: Sanitization Group 2B - Individual Chapters (Part 2)

## Objective
Clean tokenization artifacts and ghost characters in the second half of the individual chapters.

## Target Files
- `capitulos/individual/07_mantenimiento.tex`
- `capitulos/individual/08_marco_juridico.tex`
- `capitulos/individual/09_control_de_calidad.tex`
- `capitulos/individual/10_diagramas_de_flujo.tex`
- `capitulos/individual/11_estudio_de_tiempos.tex`
- `capitulos/individual/12_localizacion.tex`
- `capitulos/individual/13_nuevosmateriales.tex`

## Protocol
For each file:
1. `read_file` $ightarrow$ 2. Clean in memory $ightarrow$ 3. `write_file`.

## QA
- Report the number of tokens cleaned per file.