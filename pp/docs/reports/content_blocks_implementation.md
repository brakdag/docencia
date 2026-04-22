# Implementation of Content Blocks for Pedagogical Roadmap

This document contains the technical content, examples, and templates requested in the work order `docs/ordenes_de_trabajo/generate_content_blocks.md`. This material is designed for 5th-year technical high school students (Electromechanics).

---

## 1. Chapter 02 (Idea) - Decision Matrix

### Tutorial: How to Build a Weighting Matrix (Matriz de Ponderación)

A Weighting Matrix is a quantitative tool used to select the best alternative among several options based on a set of predefined criteria. This removes subjectivity from the decision-making process.

**Step-by-Step Process:**
1. **Identify Alternatives**: List the possible solutions or products (e.g., Motor A, Motor B, Motor C).
2. **Define Selection Criteria**: Determine what factors are important for the project (e.g., Cost, Efficiency, Durability).
3. **Assign Weights**: Give each criterion a weight based on its importance. The sum of all weights must equal 100% (or 1.0).
4. **Score the Alternatives**: Rate each alternative for each criterion using a scale (e.g., 1 to 5, where 5 is the best).
5. **Calculate Weighted Score**: Multiply the score by the weight for each cell and sum the results for each alternative.
6. **Select the Winner**: The alternative with the highest total weighted score is the most viable option.

### Concrete Example: Selecting an Industrial Motor

**Scenario**: A project requires a motor for a conveyor belt. We are comparing a High-Efficiency Permanent Magnet Motor (Option A) and a Standard Induction Motor (Option B).

| Criterion | Weight | Option A (Score 1-5) | Option A (Weighted) | Option B (Score 1-5) | Option B (Weighted) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Energy Efficiency | 0.40 | 5 | 2.0 | 3 | 1.2 |
| Initial Cost | 0.30 | 2 | 0.6 | 5 | 1.5 |
| Maintenance Ease | 0.20 | 4 | 0.8 | 4 | 0.8 |
| Availability/Lead Time | 0.10 | 3 | 0.3 | 5 | 0.5 |
| **TOTAL** | **1.00** | | **3.7** | | **4.0** |

**Analysis**: Although Option A is significantly more efficient, Option B wins due to its lower cost and higher availability, which are critical for the current project budget and timeline.

---

## 2. Chapter 02 (Kanban) - Coordination & Security

### Industrial Team Coordination
In an industrial environment, the flow of information must be unidirectional and transparent to avoid errors in fabrication. The coordination flow follows this sequence:
1. **Task Assignment**: The Project Lead moves a card from "To Do" to "In Progress" and assigns a responsible technician.
2. **Execution & Update**: The technician performs the task. If a blocker arises (e.g., missing material), the card is marked as "Blocked" and the lead is notified immediately.
3. **Quality Verification**: Once completed, the card moves to "Review/QA". A second person or the professor verifies that the piece meets the technical drawings.
4. **Completion**: After approval, the card moves to "Done", and the component is stored in the assembly area.

### Information Security in Project Management
Technical information is a valuable asset. In professional projects, the following security protocols are mandatory:
- **Confidentiality of Technical Drawings**: Blueprints and CAD files must be stored in restricted folders. Only authorized team members should have edit access.
- **Access Control**: Use of version control (like Git) or password-protected cloud folders to prevent accidental deletions or unauthorized modifications.
- **Intellectual Property**: Students must understand that the designs created are the property of the project/institution and should not be shared externally without permission.

---

## 3. Chapter 07 (Maintenance) - Equipment Sheet

### Equipment Sheet (Ficha de Equipo) Template

**[INSTITUTION NAME] - Maintenance Department**
**EQUIPMENT TECHNICAL SHEET**

| **General Information** | | **Asset ID:** [Unique Code, e.g., MOT-001] |
| :--- | :--- | :--- |
| **Equipment Name:** | [e.g., Centrifugal Pump] | **Criticality:** [High / Medium / Low] |
| **Brand:** | [Manufacturer] | **Model:** | [Model Number] |
| **Serial Number:** | [S/N] | **Installation Date:** | [DD/MM/YYYY] |

**Technical Specifications**
- **Power/Capacity:** [e.g., 5 HP / 2kW]
- **Voltage/Current:** [e.g., 380V / 3 Phase]
- **RPM / Speed:** [e.g., 1750 RPM]
- **Dimensions:** [Length x Width x Height]
- **Weight:** [kg]
- **Lubricant Type:** [e.g., ISO VG 68]

**Maintenance Plan**
| Task | Frequency | Responsible | Procedure Reference |
| :--- | :---: | :---: | :--- |
| Visual Inspection | Weekly | Operator | Manual Sec. 2.1 |
| Lubrication | Monthly | Technician | Manual Sec. 4.5 |
| Electrical Testing | Quarterly | Electrician | Norm IEC 60364 |
| Full Overhaul | Annual | External Co. | Service Contract |

**Vendor/Manufacturer Contact**
- **Company:** [Name]
- **Contact Person:** [Name]
- **Phone/Email:** [Contact Info]

**Observations:**
[Space for notes on recurring failures or modifications]

---

## 4. Chapter 12 (Location) - Weighted Factor Method

### Guided Exercise: Site Selection for a New Workshop

**Objective**: Determine the best location for a new electromechanical workshop among three potential sites (Site A, Site B, Site C).

**Step 1: Define Factors and Weights**
Assign weights based on the project's priorities (Total = 1.0).
- Proximity to Suppliers: 0.30
- Cost of Land/Rent: 0.20
- Availability of Skilled Labor: 0.30
- Access to Utilities (Power/Water): 0.20

**Step 2: Evaluation Table**
Score each site from 1 (Poor) to 10 (Excellent).

| Factor | Weight | Site A (Score) | Site A (Weighted) | Site B (Score) | Site B (Weighted) | Site C (Score) | Site C (Weighted) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Suppliers | 0.30 | 8 | 2.4 | 6 | 1.8 | 9 | 2.7 |
| Cost | 0.20 | 5 | 1.0 | 9 | 1.8 | 4 | 0.8 |
| Labor | 0.30 | 7 | 2.1 | 7 | 2.1 | 6 | 1.8 |
| Utilities | 0.20 | 9 | 1.8 | 5 | 1.0 | 8 | 1.6 |
| **TOTAL** | **1.00** | | **7.3** | | **6.7** | | **6.9** |

**Conclusion**: Site A is the optimal choice with a score of 7.3, offering the best balance between utility access and supplier proximity, despite not being the cheapest option.

---

## 5. Chapter 13 (New Materials) - Restructure

### Section A: Material Properties Guide
To select a material for an industrial component, we must analyze three fundamental dimensions:

1. **Mechanical Properties**: How the material reacts to physical forces.
   - *Tensile Strength*: Maximum stress it can withstand before breaking.
   - *Hardness*: Resistance to surface indentation or scratching.
   - *Elasticity (Young's Modulus)*: Ability to return to original shape after deformation.

2. **Thermal Properties**: How the material reacts to heat.
   - *Thermal Conductivity*: Ability to transfer heat (High for heat sinks, low for insulators).
   - *Coefficient of Thermal Expansion*: How much the material grows when heated (critical for precision fits).
   - *Melting Point*: Temperature at which it turns to liquid.

3. **Chemical Properties**: How the material reacts with its environment.
   - *Corrosion Resistance*: Ability to resist oxidation (e.g., Stainless Steel vs Carbon Steel).
   - *Chemical Inertness*: Lack of reactivity with acids or bases.

### Section B: Comparison Matrix Tutorial
When the project requires a specific property (e.g., "must be lightweight but strong"), follow this process:
1. **List Requirements**: (e.g., Weight < 2kg, Strength > 500MPa, Cost < $100).
2. **Identify Candidates**: (e.g., Aluminum 6061, Carbon Fiber, Titanium Grade 5).
3. **Create Comparison Matrix**: Score each material against the requirements.
4. **Trade-off Analysis**: If no material meets all criteria, decide which requirement can be relaxed (e.g., "I can pay more for Carbon Fiber to get the required weight").

### Section C: R&D Planning Guide for Material Trials
When testing a new material (e.g., a 3D printed composite), use this methodology:

**Phase 1: Milestones** $\rightarrow$ Define the goal (e.g., "Replace steel bracket with reinforced polymer to reduce weight by 30%").
**Phase 2: Characterization** $\rightarrow$ Perform tests on samples (Tensile tests, hardness tests, thermal cycling).
**Phase 3: Viability** $\rightarrow$ Analyze cost of production vs. performance gain. Is the material available in the local market?
**Phase 4: Sustainability** $\rightarrow$ Evaluate the environmental impact. Is it recyclable? Is the production process toxic?

---

## 6. Redundancy Cleanup List

The following questions from the `individual` chapters are now redundant because they are covered by the `proyecto` activities and should be removed from the theoretical questionnaires:

- **Chapter 07 (Mantenimiento)**:
  - "¿Qué es una ficha de equipo?"
  - "¿Porqué es importante tener una ficha de equipo de mantenimiento?"
  - (These are now handled by the actual creation of the Equipment Sheet in the project chapter).

- **Chapter 13 (Nuevos Materiales)**:
  - "¿Cuál es el papel de la nanotecnologón en la creación de nuevos materiales?"
  - "¿Cómo se fabrica la fibra de carbono y cuáles son sus aplicaciones?"
  - (These are now integrated into the Material Properties and Comparison Matrix analysis in the project chapter).
