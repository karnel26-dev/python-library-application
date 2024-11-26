import json
from .db import session


class LibraryCRUD:
    def __init__(self):
        pass

    def get_book_by_id(self, book_id: str):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        book = books.get(book_id)
        if not book:
            raise Exception('Нет книги с указанным ID')
        return book

    def book_list(self):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books',{})
        return books

    def get_books_by_title(self, title: str):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['title'].find(title) != -1:
                result[book] = books[book]
        return result

    def get_books_by_author(self, author: str):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['author'].find(author) != -1:
                result[book] = books[book]
        return result

    def get_books_by_year(self, year: str):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['year'] == year:
                result[book] = books[book]
        return result

    def get_book_status(self, book_id: str):
        try:
            book = self.get_book_by_id(book_id)
        except Exception as err:
            print(err)
            book = None
        if book:
            status = book['status']
            return status

    def book_change_status(self, book_id: str, status: str):
        session.seek(0)
        data = json.loads(session.read())
        book =  self.get_book_by_id(book_id)
        if book:
            book['status'] = status
            book_obj = {book_id: book}
            data['library']['books'].update(book_obj)
            session.seek(0)
            json.dump(data, session, indent=2, ensure_ascii=False)
            return True

    def book_add(self, book_id: str, title: str, author: str, year: str):
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

    def book_delete(self, book_id: str):
        pass
