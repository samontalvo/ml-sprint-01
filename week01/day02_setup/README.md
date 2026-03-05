# Week 01 - Day 02 (Tuesday): Sprint Project Setup

## Goals
- Create a Python virtual environment (venv)
- Install project dependencies from `requirements.txt`
- Download and place the Olist dataset in the expected `dataset/` folder
- Validate extraction step and run tests

## What I did
- Created and activated `.venv` using **Python 3.10**.
- Installed dependencies:
  - `pip install -r requirements.txt`
- Downloaded the Olist dataset and placed CSVs under `assignment/dataset/` (kept locally, not committed).
- Ran tests:
  - `pytest tests/test_extract.py` ✅ (2 passed)
- Ran the notebook section **1. Extract** successfully.

## Notes / Troubleshooting
- Python 3.14 caused issues installing pandas/matplotlib. Switching to Python 3.10 solved it.
- Jupyter may cache old code; restarting the kernel reloads updated modules.

## Commands used
```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pytest tests/test_extract.py -q