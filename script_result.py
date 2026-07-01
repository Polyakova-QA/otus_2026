import csv
import json
from pathlib import Path
from script import read_json, write_json
from script_csv import read_csv

BASE_DIR = Path(__file__).resolve().parent

users = read_json("users.json")
books = read_csv("books.csv")
books_per_user = len(books) // len(users)

# распеределяем все книги между пользователями
current_user = 0
for user in users:
    user["book"] = []

for book in books:
    user = users[current_user]
    user["book"].append(book)
    current_user += 1
    if current_user > (len(users) - 1):
        current_user = 0

result = []
for user in users:
    new_books = []
    for book in user["book"]:
        new_books.append(
            {
                "title": book["Title"],
                "author": book["Author"],
                "pages": int(book["Pages"]),
                "genre": book["Genre"],
            }
        )
    result.append(
        {
            "name": user["name"],
            "gender": user["gender"],
            "age": user["age"],
            "address": user["address"],
            "books": new_books,
        }
    )


write_json("result.json", result)
