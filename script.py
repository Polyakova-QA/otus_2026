import json
from typing import Union
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def read_json(filename: str) -> Union[list, dict]:
    with open(BASE_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(filename: str, data: dict) -> None:
    with open(BASE_DIR / filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    data = read_json("users.json")
    print(f"Loaded {len(data)} users from JSON")
    for user in data:
        print("Читаем данные о пользователях\n")
        for k, v in user.items():
            print(f"{k}: {v}")
