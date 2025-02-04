class Book:
    """
    Класс, представляющий книгу.
    """
    def __init__(self, id_, name, pages):
        """
        Инициализация объекта "Книга".

        :param id_: Уникальный идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строковое представление книги.
        """
        return f'\u041a\u043d\u0438\u0433\u0430 \"{self.name}\"'

    def __repr__(self):
        """
        Возвращает строку, создающую экземпляр книги.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    """
    Класс, представляющий библиотеку книг.
    """
    def __init__(self, books=None):
        """
        Инициализация объекта "Библиотека".

        :param books: Список книг (по умолчанию - пустой список)
        """
        self.books = books if books is not None else []

    def get_next_book_id(self):
        """
        Возвращает следующий доступный идентификатор книги.
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги по ее идентификатору.

        :param book_id: Идентификатор книги
        :return: Индекс книги в списке
        :raise ValueError: Если книга с запрашиваемым id не существует
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("\u041a\u043d\u0438\u0433\u0438 \u0441 \u0437\u0430\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0435\u043c\u044b\u043c id \u043d\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442")

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))
