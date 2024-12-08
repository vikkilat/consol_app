from enum import Enum
from book import Book
from json_storage import load_books, save_books


class MenuOption(Enum):
    ADD_BOOK = 1
    DELETE_BOOK = 2
    FIND_BOOK = 3
    SHOW_ALL_BOOKS = 4
    CHANGE_STATUS = 5
    EXIT = 6

    def description(self):
        descriptions = {
            MenuOption.ADD_BOOK: "Добавить книгу",
            MenuOption.DELETE_BOOK: "Удалить книгу",
            MenuOption.FIND_BOOK: "Найти книгу",
            MenuOption.SHOW_ALL_BOOKS: "Показать все книги",
            MenuOption.CHANGE_STATUS: "Изменить статус книги",
            MenuOption.EXIT: "Выход"
        }
        return descriptions.get(self, "Неизвестная опция")


books = load_books()


def add_book(title, author, year):
    """Добавляет книгу в библиотеку."""
    book = Book(title=title, author=author, year=year)
    books.append(book)
    save_books(books)
    print(f"Книга '{title}' добавлена в библиотеку.")


def delete_book(book_id):
    """Удаляет книгу из библиотеки по ID."""
    global books
    book_to_delete = next((book for book in books if book.id == book_id), None)
    if book_to_delete is None:
        print(f"Книга с ID '{book_id}' не найдена в библиотеке.")
        return
    books = [book for book in books if book['id'] != book_id]
    save_books()
    print(f"Книга с ID '{book_id}' удалена из библиотеки.")


def find_books(keyword):
    """Ищет книги по названию, автору или году."""
    return [
        book
        for book in books
        if keyword.lower() in book.title.lower()
        or keyword.lower() in book.author.lower()
        or str(book.year) == keyword
    ]


def display_books():
    """Отображает все книги в библиотеке."""
    if not books:
        print("Нет книг в библиотеке.")
        return
    for book in books:
        print(f"""ID: {book.id},
        название книги: {book.title},
        автор книги: {book.author},
        год издания: {book.year},
        статус: {book.status}""")


def change_status(book_id, new_status):
    """Изменяет статус книги по ID."""
    valid_statuses = ["в наличии", "выдана"]
    for book in books:
        if book.id == book_id:
            if new_status not in valid_statuses:
                print("Недопустимый статус. Статус должен быть 'в наличии' или 'выдана'.")
                return
            else:
                book.status = new_status
                save_books(books)
                print(f"Статус книги '{book.title}' изменен на '{new_status}'.")
                return
    print("Книга с таким ID не найдена.")


def show_menu():
    print("\nМеню:")
    for option in MenuOption:
        print(f"{option.value}. {option.description()}")


def library():
    while True:
        show_menu()
        try:
            choice = MenuOption(int(input("Выберите действие: ")))
        except ValueError:
            print("Некорректный выбор. Попробуйте снова.")
            continue

        if choice == MenuOption.ADD_BOOK:
            while True:
                title = input("Введите название книги: ")
                if not title:
                    print("Название книги не может быть пустым. Попробуйте снова.")
                    continue
                author = input("Введите автора книги: ").strip()
                if not author:
                    print("Автор книги не может быть пустым. Попробуйте снова.")
                    continue
                try:
                    year = int(input("Введите год издания книги: ").strip())
                    if year <= 0:
                        print("Год издания должен быть положительным числом. Попробуйте снова.")
                        continue
                except ValueError:
                    print("Некорректный ввод года. Попробуйте снова.")
                    continue
                break
            add_book(title, author, year)

        elif choice == MenuOption.DELETE_BOOK:
            book_id = input("Введите ID книги для удаления: ").strip()
            delete_book(book_id)

        elif choice == MenuOption.FIND_BOOK:
            keyword = input("Введите название, автора или год издания для поиска: ").strip()
            results = find_books(keyword)
            if results:
                global books
                books = results
                display_books()
                books = load_books()
            else:
                print("Книги не найдены.")

        elif choice == MenuOption.SHOW_ALL_BOOKS:
            display_books()

        elif choice == MenuOption.CHANGE_STATUS:
            book_id = input("Введите ID книги для изменения статуса: ").strip()
            new_status = input("Введите новый статус (в наличии/выдана): ").strip()
            change_status(book_id, new_status)

        elif choice == MenuOption.EXIT:
            print("Выход из программы...")
            break


if __name__ == "__main__":
    library()
