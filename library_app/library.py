import uuid

from library_app import validators
from .crud import crud
from .db import Session


class LibraryApp:
    def __init__(self, session: Session) -> None:
        self.session = session

    def book_add(self, title: str, author: str, year: str) -> None:
        """
        creating a book object and passing it to the crud module for create
        :param title: title of a book
        :param author: author of a book
        :param year: year of a book publication
        :return: None
        """
        book_id = str(uuid.uuid4().int)[:8]
        title = title
        author = author
        year = validators.validate_year(year)
        return crud.book_add(self.session, book_id, title, author, year)

    def book_delete(self, book_id: str) -> bool:
        """
        validating book_id and getting a book object and passing it to the crud module for delete
        :param book_id: id of a book
        :return: True if success, else False
        """
        try:
            book_id = validators.validate_book_id(self.session, book_id)
        except ValueError as err:
            print(err)
            return False
        try:
            crud.get_book_by_id(self.session, book_id)
            crud.book_delete(self.session, book_id)
            return True
        except:
            print('Такой книги нет')
            return False

    def get_book_status(self, book_id : str) -> None:
        """
        validating book_id and getting book status
        :param book_id:
        :return: None or Exception
        """
        try:
            book_id = validators.validate_book_id(self.session, book_id)
            return crud.get_book_status(self.session, book_id)
        except ValueError as err:
            print(err)
        try:
            book_status = crud.get_book_status(self.session, book_id)
            return book_status
        except ValueError as err:
            print(err)

    def book_search_title(self, title: str) -> dict:
        """
        search a book by book status
        :param title: title of a book
        :return: dict with book info
        """
        return crud.get_books_by_title(self.session, title)

    def book_search_author(self, author: str) -> dict:
        """
        search a book by book author
        :param author: author of a book
        :return: dict with book info
        """
        return crud.get_books_by_author(self.session, author)

    def book_search_year(self, year: str) -> dict:
        """
        search a book by book year publication
        :param year: year of a book publication
        :return: dict with book info
        """
        try:
            year = validators.validate_year(year)
            return crud.get_books_by_year(self.session, year)
        except ValueError as err:
            print(err)
            return {}

    def book_list(self) -> dict:
        """
        getting list of a books
        :return: dict with books info
        """
        return crud.book_list(self.session)

    def book_change_status(self, book_id: str, status: str) -> bool:
        """
        Validating book_id and change a books status
        :param book_id: id of a book
        :param status: new book status
        :return: True if success, else False
        """
        try:
            book_id = validators.validate_book_id(self.session, book_id)
        except ValueError as err:
            return False
        try:
            status =  validators.validate_status(status)
        except ValueError as err:
            return False

        current_book_status = crud.get_book_status(self.session, book_id)
        if status == current_book_status:
            print('Текущий статус совпадает с выбранным!')
            return False
        return crud.book_change_status(self.session, book_id, status)
