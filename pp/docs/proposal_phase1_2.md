# Technical Proposal: Phase 1 & 2 Reinforcement

**Author**: Technical Content Editor
**Status**: Draft for Pedagogical Review

## 1. Addition to Chapter: Fixed Costs
### Topic: The Break-even Point (Punto de Equilibrio)

**Technical Content to be added:**

"The **Break-even Point** is the level of production or sales at which the total revenues equal the total costs (both fixed and variable). At this point, the company neither makes a profit nor incurs a loss.

To calculate the break-even point in units ($Q$), the following formula is used:

$$Q = \frac{CF}{P - CV}$$

Where:
- **$Q$**: Break-even quantity (units to be produced/sold).
- **$CF$**: Total Fixed Costs (the constant costs regardless of production).
- **$P$**: Unit Selling Price (the price at which each unit is sold).
- **$CV$**: Unit Variable Cost (the cost that varies directly with each unit produced).

The difference $(P - CV)$ is known as the **Contribution Margin per unit**, which is the amount of money from each sale that contributes to covering the fixed costs."

---

## 2. Addition to Chapter: Project Planning
### Topic: Step-by-Step PERT Calculation Guide

**Technical Content to be added:**

"To determine the project duration and the critical path, we use two main calculation passes:

### A. The Forward Pass (Calculating Early Times)
Used to find the earliest possible time an activity can start (**ES**) and finish (**EF**).
1. **Start**: The first activity has $ES = 0$.
2. **Calculation**: $EF = ES + Duration$.
3. **Succession**: The $ES$ of a subsequent activity is the $EF$ of its predecessor. If an activity has multiple predecessors, its $ES$ is the **maximum** $EF$ of all its predecessors.

### B. The Backward Pass (Calculating Late Times)
Used to find the latest possible time an activity can start (**LS**) and finish (**LF**) without delaying the project.
1. **End**: The last activity's $LF$ is equal to its $EF$ (the project duration).
2. **Calculation**: $LS = LF - Duration$.
3. **Precedence**: The $LF$ of a preceding activity is the $LS$ of its successor. If an activity is a predecessor to multiple tasks, its $LF$ is the **minimum** $LS$ of all its successors.

### C. Slack (Holgura) and Critical Path
- **Slack**: The amount of time an activity can be delayed without delaying the project. Formula: $Slack = LF - EF$ (or $LS - ES$).
- **Critical Path**: The sequence of activities where $Slack = 0$. Any delay in these activities directly delays the entire project."

**Proposed Solved Example (Simplified):**
- Activity A (Dur: 3, Pred: -) $ightarrow$ ES:0, EF:3
- Activity B (Dur: 2, Pred: A) $ightarrow$ ES:3, EF:5
- Activity C (Dur: 4, Pred: A) $ightarrow$ ES:3, EF:7
- Activity D (Dur: 1, Pred: B, C) $ightarrow$ ES:max(5,7)=7, EF:8

*Backward Pass for D*: LF:8, LS:7 $ightarrow$ *For C*: LF:7, LS:3 $ightarrow$ *For B*: LF:7, LS:5 $ightarrow$ *For A*: LF:min(3,5)=3, LS:0.

*Critical Path*: A $ightarrow$ C $ightarrow$ D (Slack = 0).