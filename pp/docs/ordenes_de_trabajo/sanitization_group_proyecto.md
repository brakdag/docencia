# Work Order: Sanitization Group 3 - Project Chapters

## Objective
Clean tokenization artifacts and ghost characters in all project implementation chapters.

## Target Files
All `.tex` files in `capitulos/proyecto/`.

## Protocol
To ensure absolute stability and avoid timeouts, process files in small groups (max 3 per instance) using the following sequence:
1. `read_file` $ightarrow$ 2. Clean in memory $ightarrow$ 3. `write_file`.

## QA
- Report the number of tokens cleaned per file.