# Sequential Workflow Protocol

## Overview
This document defines the operational procedure for executing tasks within the project. To ensure maximum coherence, maintain a clear audit trail, and optimize token consumption (TPM), the project adopts a **Strictly Linear Execution Model**. 

## The Invocation Mechanism
As the Global Orchestrator, the Electromechanical Professor manages the staff by invoking specialized instances. Each specialist is activated using the following parameter:

`-fsi "docs/staff/[role_file].md"

This command ensures that the invoked instance is fully initialized with the specific responsibilities, competencies, and constraints of the assigned role before beginning work.

## The Linear Execution Pipeline
Tasks must move through the pipeline in a sequential, one-at-a-time manner. No parallel consultations are permitted. The standard sequence is as follows:

1. **Orchestration Phase (Professor)**: 
   - Analyze the Project Lead's request.
   - Define the specific scope for each specialist.
   - Establish the sequence of intervention.

2. **Technical Validation Phase (Technical Content Editor)**:
   - Invoked via `-fsi "docs/staff/technical_content_editor.md"
   - Focuses on technical accuracy and electromechanical rigor.
   - Output: Technically validated content.

3. **Pedagogical Refinement Phase (Pedagogical Consultant)**:
   - Invoked via `-fsi "docs/staff/pedagogical_consultant.md"
   - Focuses on instructional design, timing, and student accessibility.
   - Output: Pedagogically optimized content.

4. **Authority Approval Phase (Project Lead)**:
   - The synthesized result is presented to the Project Lead.
   - **Crucial**: No further movement occurs until explicit consent is granted.

5. **Technical Implementation Phase (LaTeX & TikZ Specialist)**:
   - Invoked via `-fsi "docs/staff/latex_specialist.md"
   - Translates approved content into LaTeX code and TikZ graphics.
   - Output: Updated `.tex` files and compiled PDF.

6. **Final Quality Assurance (Professor & Lead)**:
   - Final review of the PDF to ensure the global vision is intact.

## Operational Constraints
- **No Parallelism**: Only one specialist instance may be active at a time. A task must be completed and the instance closed before the next specialist is called.
- **Token Management**: This linear approach is mandatory to prevent TPM spikes and avoid context fragmentation in the LLM thread.
- **State Transfer**: The Global Orchestrator is responsible for carrying the output of one phase as the input for the next, ensuring no information is lost between instances.

## Summary of Flow
`Lead Request` $ightarrow$ `Professor` $ightarrow$ `Tech Editor` $ightarrow$ `Pedagogue` $ightarrow$ `Lead Approval` $ightarrow$ `LaTeX Specialist` $ightarrow$ `Final PDF`