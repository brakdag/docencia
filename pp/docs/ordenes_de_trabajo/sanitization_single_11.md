# Work Order: Single-File Sanitization - 11_estudio_de_tiempos.tex

## Objective
Clean tokenization artifacts and ghost characters in a single file.

## Target File
- `capitulos/individual/11_estudio_de_tiempos.tex`

## Protocol
1. `read_file` the target file.
2. Identify any alphanumeric noise (e.g., `OOf3n`, `0ficas`, `ónLamos`) or hidden characters.
3. Apply corrections in memory.
4. `write_file` the entire cleaned content back to the path.

## QA
- Report the number of tokens cleaned.