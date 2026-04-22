# Work Order: Implementation of Linguistic Audit Corrections

## Objective
Correct tokenization errors, typos, and technical inaccuracies identified during the Linguistic and Technical Audit.

## Source Material
- **Audit Report**: `docs/reports/linguistic_audit_report.md`

## Critical Technical Instruction
**DO NOT use `replace_string`**. To avoid the error loops encountered previously, follow this exact sequence for every file:
1. `read_file` the target `.tex` file.
2. Apply the corrections in memory.
3. `write_file` the entire updated content back to the path.

## Required Corrections

### 1. `capitulos/individual/01_gantt.tex`
- Change "Tiempos Tardóos" $\rightarrow$ "Tiempos Tardíos"
- Change "\textit{Last} (Tardóo)" $\rightarrow$ "\textit{Last} (Tardío)"

### 2. `capitulos/individual/09_control_de_calidad.tex`
- Change "es asóC que sale los métodos de 4M, 5M, 6M o /M" $\rightarrow$ "así surgen los métodos de 4M, 5M, 6M o 7M"

### 3. `capitulos/individual/11_estudio_de_tiempos.tex`
- Change "referónLamos" $\rightarrow$ "referimos"

### 4. `capitulos/individual/12_localizacion.tex`
- Change "topografón" $\rightarrow$ "topografía"

### 5. `capitulos/individual/13_nuevosmateriales.tex`
- Change "específ0ficas" $\rightarrow$ "específicas"
- Verify that "Expansión" is correctly encoded (UTF-8).

## QA
- Ensure no other text was accidentally modified.
- Verify that the document compiles without errors.