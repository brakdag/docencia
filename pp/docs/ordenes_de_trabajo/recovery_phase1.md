# Work Order: Phase 1 Recovery (Failed Files)

## Objective
Complete the pending updates for Chapter 02 files that failed in the previous attempt.

## Source Material
- `docs/reports/content_blocks_implementation.md`

## Critical Technical Instruction
**DO NOT use `replace_string`**. To ensure the content is inserted correctly, follow this exact sequence:
1. `read_file` the target `.tex` file.
2. Construct the updated version of the file in your memory, inserting the new content from the source material in the appropriate sections.
3. `write_file` the entire updated content back to the path.

## Pending Tasks

### 1. Chapter 02 (Idea) - `capitulos/individual/02_idea.tex`
- Insert "Tutorial: How to Build a Weighting Matrix" and the "Concrete Example: Selecting an Industrial Motor" before the activities section.

### 2. Chapter 02 (Kanban) - `capitulos/individual/02_kanban.tex`
- Add "Industrial Team Coordination" and "Information Security in Project Management" as new subsections before the practical exercises.

## QA
- Verify that the LaTeX syntax remains valid.