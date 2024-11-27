import json


class LibraryCRUD:
    def get_book_by_id(self, session, book_id: str):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        book = books.get(book_id)
        return book

    def book_list(self, session):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books',{})
        return books

    def get_books_by_title(self, session, title: str):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['title'].find(title) != -1:
                result[book] = books[book]
        return result

    def get_books_by_author(self, session, author: str):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['author'].find(author) != -1:
                result[book] = books[book]
        return result

    def get_books_by_year(self, session, year: str):
        session.seek(0)
        data = json.loads(session.read())
        books = data.get('library', {}).get('books', {})
        result = {}
        for book in books:
            if books[book]['year'] == year:
                result[book] = books[book]
        return result

    def get_book_status(self, session, book_id: str):
        try:
            book = self.get_book_by_id(session, book_id)
        except Exception as err:
            print(err)
            book = None
        if book:
            status = book['status']
            return status

    def book_change_status(self, session, book_id: str, status: str):
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

    def book_add(self, session, book_id: str, title: str, author: str, year: str):
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

    def book_delete(self, session, book_id: str):
        session.seek(0)
        data = json.loads(session.read())
        del data['library']['books'][book_id]
        session.seek(0)
        session.truncate()
        json.dump(data, session, indent=2, ensure_ascii=False)


crud = LibraryCRUD()