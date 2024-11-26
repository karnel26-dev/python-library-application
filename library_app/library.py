import uuid
from library_app import validators

from .crud import LibraryCRUD


crud = LibraryCRUD()

class LibraryApp:
    def __init__(self):
        pass

    def book_add(self, title: str, author: str, year: str):
        book_id = str(uuid.uuid4().int)[:8]
        title = title
        author = author
        year = validators.validate_year(year)
        crud.book_add(book_id, title, author, year)

    def book_delete(self, book_id: str):
        book_id = validators.validate_book_id(book_id)
        crud.book_delete(book_id)

    def book_search_title(self, title: str):
        return crud.get_books_by_title(title)

    def book_search_author(self, author: str):
        return crud.get_books_by_author(author)

    def get_book_status(self, book_id : str):
        book_status = crud.get_book_status(book_id)
        if book_status:
            return crud.get_book_status(book_id)

    def book_search_year(self, year: str):
        try:
            year = validators.validate_year(year)
            return crud.get_books_by_year(year)
        except ValueError as err:
            print(err)
            return {}

    def book_list(self):
        return crud.book_list()

    def book_change_status(self, book_id: str, status: str):
        try:
            book_id = validators.validate_book_id(book_id)
            status =  validators.validate_status(status)
            current_book_status = crud.get_book_status(book_id)
            if status == current_book_status:
                raise Exception('Текущий статус совпадает с выбранным!')
            return crud.book_change_status(book_id, status)
        except Exception as err:
            print(err)
            return None