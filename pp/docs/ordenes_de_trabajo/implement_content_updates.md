# Work Order: Implementation of Pedagogical Content Updates

## Objective
Integrate the new technical content, tutorials, and templates into the LaTeX source files to align the guide with the approved Pedagogical Roadmap.

## Source Material
- **Content Source**: `docs/reports/content_blocks_implementation.md`

## Implementation Instructions

### 1. Chapter 02 (Idea) - `capitulos/individual/02_idea.tex`
- **Action**: Insert the "Tutorial: How to Build a Weighting Matrix" and the "Concrete Example: Selecting an Industrial Motor" before the student activities section.
- **Formatting**: Use a `tcolorbox` or a similar highlighted block for the tutorial steps to make it visually distinct.

### 2. Chapter 02 (Kanban) - `capitulos/individual/02_kanban.tex`
- **Action**: Add the sections "Industrial Team Coordination" and "Information Security in Project Management" as new subsections before the practical exercises.

### 3. Chapter 07 (Maintenance) - `capitulos/individual/07_mantenimiento.tex`
- **Action**: Implement the "Equipment Sheet (Ficha de Equipo) Template". 
- **Formatting**: This should be rendered as a professional table/form that looks like a real industrial document. Use `tabularx` or `longtable` to ensure it fits the page.

### 4. Chapter 12 (Location) - `capitulos/individual/12_localizacion.tex`
- **Action**: Insert the "Guided Exercise: Site Selection for a New Workshop" including the evaluation table.

### 5. Chapter 13 (New Materials) - `capitulos/individual/13_nuevosmateriales.tex`
- **Action**: **Complete Overhaul**. Replace the existing material catalog with the three new sections:
    - Section A: Material Properties Guide
    - Section B: Comparison Matrix Tutorial
    - Section C: R&D Planning Guide for Material Trials
- **Formatting**: Use clear hierarchical headings and bullet points for the properties.

### 6. Redundancy Cleanup (Various Files)
- **Action**: Search for and remove the following questions from the theoretical questionnaires in the `individual` chapters:
    - In `capitulos/individual/07_mantenimiento.tex`: Remove questions about "What is an equipment sheet?" and its importance.
    - In `capitulos/individual/13_nuevosmateriales.tex`: Remove questions about nanotechnology and carbon fiber manufacturing processes.

## Quality Assurance
- Ensure all new tables are properly centered and captioned.
- Maintain consistency in font sizes and styles as per `sty/config.sty`.
- Verify that the document still compiles without errors after these insertions.