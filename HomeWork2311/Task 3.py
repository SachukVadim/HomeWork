import pickle
import json

products = [
    {"id": 1, "name": "Ноутбук", "price": 25000, "category": "Електроніка"},
    {"id": 2, "name": "Смартфон", "price": 15000, "category": "Електроніка"},
    {"id": 3, "name": "Навушники", "price": 2000, "category": "Аксесуари"},
    {"id": 4, "name": "Смарт-годинник", "price": 8000, "category": "Гаджети"},
]

with open("products.pkl", "wb") as pickle_file:
    pickle.dump(products, pickle_file)
print("Дані збережено у форматі pickle (products.pkl).")

with open("products.json", "w", encoding="utf-8") as json_file:
    json.dump(products, json_file, ensure_ascii=False, indent=4)
print("Дані збережено у форматі JSON (products.json).")
