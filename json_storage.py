import json
import os
from book import Book  # Импортируем класс Book из основного модуля

FILE_NAME = "library.json"


def load_books():
    """Загружает книги из файла или создает новый файл, если его нет."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        print(f"Создан новый файл библиотеки: {FILE_NAME}")
        return []
    else:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return [Book.from_dict(book) for book in json.load(file)]


def save_books(books):
    """Сохраняет книги в файл."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump([book.to_dict() for book in books], file, ensure_ascii=False, indent=4)
