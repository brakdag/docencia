# Work Order: Global Tokenization and Encoding Sanitization

## Objective
Perform a deep, character-level cleaning of all LaTeX source files to eliminate tokenization artifacts, AI-ghost characters, and encoding corruptions (e.g., "infomaciOOf3n", "tardóos", "específ0ficas").

## Scope
All `.tex` files in the following directories:
- `capitulos/comun/`
- `capitulos/individual/`
- `capitulos/proyecto/`

## Execution Instructions

### 1. The Deep Scan
Scan every file looking for patterns of corruption. Do not read for meaning; read for **anomalies**. Specifically look for:
- Alphanumeric noise inside Spanish words (e.g., `OOf3n`, `0ficas`, `ónLamos`).
- Misplaced or double accents.
- Hidden control characters (U+0008, ^^H, etc.).
- Any sequence that looks like a tokenization failure.

### 2. The Cleaning Process
For every file where anomalies are found:
1. `read_file` the target `.tex` file.
2. Apply all corrections in memory using a mapping of [Corrupt Pattern $ightarrow$ Correct Word].
3. `write_file` the entire cleaned content back to the path.

### 3. Reporting
Provide a final summary in the form of a list:
- `File Path`: [Number of tokens cleaned] - [Example of a fixed word].

## Critical Constraint
**DO NOT use `replace_string`**. Use the `read_file` $ightarrow$ `write_file` pattern to ensure absolute integrity of the file and avoid matching errors.