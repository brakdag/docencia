# Work Order: Sanitization Batch 1 - Common Files

## Objective
Clean tokenization artifacts and ghost characters in the common chapters.

## Target Files
- `capitulos/comun/00_a_portada.tex`
- `capitulos/comun/00_b_introduccion.tex`
- `capitulos/comun/00_c_planificacion.tex`
- `capitulos/comun/00_d_acuerdo.tex`
- `capitulos/comun/14_formulariopasantias.tex`
- `capitulos/comun/99_bibliografia.tex`

## Protocol
1. `read_file` $ightarrow$ 2. Clean in memory $ightarrow$ 3. `write_file`.