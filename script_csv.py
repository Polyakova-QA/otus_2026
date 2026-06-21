import csv
from pathlib import Path
from typing import List, Dict

BASE_DIR = Path(__file__).resolve().parent


def read_csv(filename: str) -> List[Dict]:
    file_path = BASE_DIR / filename
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_csv(
    filename: str,
    data: List[Dict],
    fieldnames: List[str],
    method="w",
    write_headers=True,
) -> None:
    file_path = BASE_DIR / filename
    with open(file_path, method, encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_headers:
            writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    data = read_csv("books.csv")
    for book in data:
        for k, v in book.items():
            print(f"{k}: {v}")
