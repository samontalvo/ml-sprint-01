# ML Sprint 01

Repository to track my progress in an ML Developer program: daily assignments, sprint projects, and notes.

## Structure
- `week01/` - Python warm-up, Pandas, APIs, project setup
- `week02/` - SQL, databases, pipelines
- `week03/` - EDA, feature engineering, visualization

## Week 01 Highlights

### Day 01 — Python Assignment: Text Analysis (Argentina Names 1922–2015)
Using pure Python (standard library only) to analyze a dataset of registered names (grouped by name and year).

**Key results (from my run):**
- **Q1:** People registered each year (printed as year → total).
- **Q2 (shortest name):** `P` — length: **1** — year: **1972** — position: **3423316**
- **Q3 (largest name):** `RobertoCarlos(antesDeCumplimentarHablarConAugustoBorjaCdr--jujuy0388-4310036)` — length: **76** — position: **3869076**
- **Q4 (palindrome exists?):** **Yes** — name: `Ana` — year: **1922** — count: **113** — line: **7**
- **Q5 (most registered name):** **Juan Carlos** — total across all years: **2,890,607**

> Note: the dataset file is not included in the repository due to its size.

## How to run
Most exercises are in Python scripts or Jupyter notebooks.  
Example (Day 01):

```bash
cd week01/day01_text_analysis
python text_analysis.py --file data/registered-names-1922-2015.csv