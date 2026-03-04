import csv 
import re
from collections import defaultdict 

def people_registered_per_year(csv_path: str) -> dict[int, int]:
    totals = defaultdict(int)
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        contador = 100000
        for idx,row in enumerate(reader):
            year = int(row["year"])
            count = int(row["count"])
            totals[year] += count
            if idx == contador:
                break
    return dict(sorted(totals.items()))

def shortest_name_in_dataset(csv_path: str) -> str:
    shortest_name = None
    position = None
    year = None
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row_index, row in enumerate(reader, start=2):
            name = row["name"].strip().replace(" ","")
            if not name:
                continue
            if shortest_name is None:
                shortest_name = name
                continue
            if len(name) < len(shortest_name):
                shortest_name = name
                year = int(row["year"])
                position = row_index
    return shortest_name, year, position

def largest_name_in_dataset(csv_path: str) -> str:
    largest_name = None
    position = None
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row_index, row in enumerate(reader, start=2):
            name = row["name"].strip().replace(" ","")
            if not name:
                continue
            if largest_name is None:
                largest_name = name
                continue
            if len(name) > len(largest_name):
                largest_name = name
                position = row_index
    return largest_name, position

def is_palindrome(text: str) -> bool:
    cleaned = text.strip().lower()
    cleaned = re.sub(r"\s+", "",cleaned)
    return cleaned == cleaned[::-1] and cleaned !=""

def find_first_palindrome_name(csv_path: str):
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for line_num, row in enumerate(reader, start=2):
            name_original = row["name"]
            if not name_original:
                continue
            if is_palindrome(name_original):
                return{
                    "name": name_original,
                    "year": int(row["year"]),
                    "count": int(row["count"]),
                    "line": line_num,
                }
    return None

def most_registered_name_total(csv_path: str):
    totals = defaultdict(int)
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"].strip()
            if not name:
                continue
            count = int(row["count"])
            totals[name] += count
    best_name = None
    best_total = -1

    for name, total in totals.items():
        if total > best_total:
            best_total = total
            best_name = name
    return {"name": best_name, "total": best_total}


if __name__ == "__main__":
    path = "data/registered-names-1922-2015.csv"
    totals_by_year = people_registered_per_year(path)
    print("===Q1. How many people were registered each year?====")
    for year, total in totals_by_year.items():
        print(year, total)

    print("===Q2. What is the shorter name in the dataset?====")
    name, year, position = shortest_name_in_dataset(path)
    print(f"Shortest name:{name} length :{len(name)} year: {year} position: {position}")

    print("===Q3. What is the largest name in the dataset?====")
    name, position = largest_name_in_dataset(path)
    print(f"Largest name:{name} length :{len(name)} position: {position}")

    print("===Q4. Is there a palindrome name?====")
    pal = find_first_palindrome_name(path)
    if pal:
        print(f"Yes! Name: {pal['name']} year: {pal['year']} count: {pal['count']} line={pal['line']}")
    else:
        print("No palindome name found")

    print("===Q5. What is the name with the largest number of people registered?====")

    best_total = most_registered_name_total(path)
    print(f"Max total across all years: {best_total['name']} | total={best_total['total']}")
