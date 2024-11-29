import json

from .db import Session


class LibraryCRUD:
    """
    Class for CRUD-operation in File database
    """
    def get_book_by_id(self, session: Session, book_id: str) -> dict:
        """
        Getting book by ID
        :param session: DB session
        :param book_id: id of a book
        :return: book object
        """
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        book = books.get(book_id)
        return book

    def book_list(self, session: Session) -> dict:
        """
        Getting a list of a books
        :param session: DB session
        :return: list of a books objects
        """
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books',{})
        return books

    def get_books_by_title(self, session: Session, title: str) -> dict:
        """
        Getting books by title of a book
        :param session: DB session
        :param title: title of a book
        :return: list of a books objects
        """
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['title'].find(title) != -1:
                result[book] = books[book]
        return result

    def get_books_by_author(self, session: Session, author: str) -> dict:
        """
        Getting books by author
        :param session: DB session
        :param author: author of a book
        :return: list of a books objects
        """
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['author'].find(author) != -1:
                result[book] = books[book]
        return result

    def get_books_by_year(self, session: Session, year: str) -> dict:
        """
        Getting books by year
        :param session: DB session
        :param year: year of a book
        :return: list of a books objects
        """
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['year'] == year:
                result[book] = books[book]
        return result

    def get_book_status(self, session: Session, book_id: str) -> str | None:
        """
        Getting status of a book
        :param session: DB session
        :param book_id: ID of a book
        :return: status of a book
        """
        try:
            book = self.get_book_by_id(session, book_id)
        except Exception as err:
            print(err)
            book = None
        if book:
            status = book['status']
            return status

    def book_change_status(self, session: Session, book_id: str, status: str) -> bool:
        """

        :param session: DB session
        :param book_id: ID of a book
        :param status: new status for the book
        :return: bool status operation
        """
        session.seek(0)
        data = json.loads(session.read())
        book =  self.get_book_by_id(session, book_id)
        if book:
            book['status'] = status
            book_obj = {book_id: book}
            data['library']['books'].update(book_obj)
            session.seek(0)
            json.dump(data, session, indent=2, ensure_ascii=False)
            return True

    def book_add(self, session: Session, book_id: str, title: str, author: str, year: str) -> bool:
        """
        Addition book in library
        :param session: DB session
        :param book_id: ID of a book
        :param title: title of a book
        :param author: author of a book
        :param year: year of a publication of a book
        :return: status of a operation
        """
        session.seek(0)
        books = json.loads(session.read())
        book_obj = {
            book_id: {
            'author': author,
            'title': title,
            'year': year,
            'status': 'В наличии'
            }
        }
        books['library']['books'].update(book_obj)
        session.seek(0)
        json.dump(books, session, indent=2, ensure_ascii=False)
        return True

    def book_delete(self, session: Session, book_id: str) -> bool:
        """
        Deleting a book
        :param session: DB session
        :param book_id: ID of a book
        :return: status of operation
        """
        session.seek(0)
        data = json.loads(session.read())
        del data['library']['books'][book_id]
        session.seek(0)
        session.truncate()
        json.dump(data, session, indent=2, ensure_ascii=False)
        return True


crud = LibraryCRUD()