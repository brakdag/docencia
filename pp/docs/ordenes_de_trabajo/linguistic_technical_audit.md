# Work Order: Comprehensive Linguistic and Technical Audit

## Objective
Perform a deep review of all LaTeX source files to eliminate "AI-generated artifacts," fix tokenization errors, and ensure the tone is natural, professional, and appropriate for 5th-year technical secondary school students.

## Scope of Analysis
All `.tex` files within the `capitulos/` directory (comun, individual, and proyecto).

## Audit Criteria

### 1. Tokenization & Encoding Errors
- Search for and correct words with misplaced accents or corrupted characters (e.g., "tardóos" $\rightarrow$ "tardíos").
- Identify any remaining Unicode or encoding artifacts that might cause compilation issues or reading difficulties.

### 2. Elimination of "AI-isms"
- **Robotic Phrasing**: Replace overly formal, repetitive, or generic AI structures (e.g., "It is important to note that...", "In conclusion, we can see that...") with direct, teacher-like instructions.
- **Redundancy**: Remove excessive adjectives or circular explanations typical of LLM outputs.
- **Natural Flow**: Ensure the transition between paragraphs feels human and purposeful.

### 3. Tone & Level Adjustment
- **Target Audience**: 17-18 year old technical students.
- **Tone**: Professional, authoritative yet accessible, and focused on practical application (workshop-oriented).
- **Directness**: Use active voice and imperative verbs for activities (e.g., "Calculate the cost" instead of "The student should proceed to calculate the cost").

### 4. Industrial Terminology Validation
- Ensure that all electromechanical terms are consistent with current industrial standards and local technical school vocabulary.

## Expected Deliverable
A detailed report in `docs/reports/linguistic_audit_report.md` containing:
- **Error Log**: A table with [File | Original Text | Corrected Text | Reason for Change].
- **General Observations**: A summary of the most common AI patterns found and how they were addressed.
- **Final Validation**: A confirmation that the text now reads as if written by a human professor of Electromechanics.