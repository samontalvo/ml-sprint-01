# Week 01 - Day 01: Python Assignment - Text Analysis (Argentina Names)

## Objective
Practice text analysis using pure Python (standard library only) by analyzing a dataset of registered names in Argentina (1922–2015).

## Dataset
File: `registered-names-1922-2015.csv` (not included in the repo due to size).

Expected columns:
- `name`
- `count`
- `year`

## Questions
1. How many people were registered each year?
2. What is the shortest name in the dataset?
3. What is the largest name in the dataset?
4. Is there a name in the database that is a palindrome?
5. What is the name with the largest number of people registered?

## Results (from my run)
- **Q1:** People registered each year (printed as `year -> total`).
- **Q2 (shortest name):** `P` — length: **1** — year: **1972** — position: **3423316**
- **Q3 (largest name):** `RobertoCarlos(antesDeCumplimentarHablarConAugustoBorjaCdr--jujuy0388-4310036)` — length: **76** — position: **3869076**
- **Q4 (palindrome exists?):** **Yes** — name: `Ana` — year: **1922** — count: **113** — line: **7**
- **Q5 (most registered name):** **Juan Carlos** — total across all years: **2,890,607**

> Note: Q1 output is long (one line per year), so it is printed in the console.

## How to run
1. Download the dataset and place it locally in `data/`:
   - `week01/day01_text_analysis/data/registered-names-1922-2015.csv`

2. Run:

```bash
python text_analysis.py --file data/registered-names-1922-2015.csv