# Operational Workflow Protocol

## Overview
This document defines the operational procedures for the coordination between the Global Orchestrator, Technical Specialists, and the LaTeX Specialist to ensure efficiency and token optimization.

## Role Responsibilities

### Global Orchestrator
- Acts as the central bridge and coordinator.
- Assigns tasks to specialists through formal work orders.
- Manages the project flow without directly manipulating technical source files.

### Technical Specialists
- Provide technical analysis, pedagogical suggestions, or corrections.
- Deliver all outputs in Markdown (`.md`) format.

### LaTeX Specialist
- Holds exclusive authority to modify `.tex` files.
- Implements changes based on the work orders and specialist reports.
- Ensures the technical integrity of the LaTeX document.

## Communication & Implementation Process

### Work Order System
To avoid direct editing of source code by non-authorized roles, the project uses a **Work Order** system:
1. **Creation**: The Orchestrator creates a Markdown file within the `docs/ordenes_de_trabajo/` directory detailing the required changes.
2. **Assignment**: The Orchestrator invokes the specialist via `run_instance`, providing the path to the work order.
3. **Execution**: The specialist processes the request and generates a report or a list of corrections in a new `.md` file.
4. **Implementation**: The Orchestrator forwards the specialist's report path to the **LaTeX Specialist**, who applies the changes to the `.tex` files.

### Token Optimization Strategy
To prevent context window saturation and reduce token consumption:
- **Indirect Processing**: The Orchestrator does not read or rewrite specialist `.md` files unless a summary is explicitly requested by the Project Lead.
- **Path-Based Communication**: Communication between agents is handled by passing file paths rather than full text content.
- **Trust-Based Validation**: Once the LaTeX Specialist confirms the implementation of a specialist's report, the Orchestrator validates the completion without re-reading the source code.

## Example Workflow: Orthographic Correction

1. **Orchestrator**: Creates a work order in `docs/ordenes_de_trabajo/review_orthography.md` listing the files to be reviewed.
2. **Orthography Specialist**: Receives the work order, analyzes the files, and creates a correction report (`correction_report.md`).
3. **Orchestrator**: Sends the path of `correction_report.md` to the **LaTeX Specialist**.
4. **LaTeX Specialist**: Applies the corrections to the `.tex` files and notifies the Orchestrator upon completion.
5. **Orchestrator**: Informs the Project Lead that the task is finished.