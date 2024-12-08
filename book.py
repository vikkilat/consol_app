import uuid


class Book:
    """Модель книги."""

    def __init__(self, title, author, year, status="в наличии", book_id=None):
        self.id = book_id or str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Преобразует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data):
        """Создает объект книги из словаря."""
        return cls(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"],
            book_id=data["id"],
        )

    def __str__(self):
        """Возвращает строковое представление книги."""
        return (
            f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, "
            f"Год: {self.year}, Статус: {self.status}"
        )
