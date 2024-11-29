import json
import os
import unittest

from library_app.library import LibraryApp


class TestLibraryCRUD(unittest.TestCase):
    def setUp(self):
        data = {
          "library": {
            "books": {
              "32336500": {
                "author": "aaa",
                "title": "aaa",
                "year": "2001",
                "status": "В наличии"
              }
            }
          }
        }
        self.session = open('book_test_db.json', 'w+')
        json.dump(data, self.session)
        self.library = LibraryApp(self.session)

    def test_book_add(self):
        self.assertTrue(self.library.book_add(title='title', author='author', year='2023'))
        self.assertRaises(ValueError, self.library.book_add, title='title', author='author', year='1')
        self.assertRaises(ValueError, self.library.book_add, title='title', author='author', year='0')
        self.assertRaises(ValueError, self.library.book_add, title='title', author='author', year='-1')
        self.assertRaises(ValueError, self.library.book_add, title='title', author='author', year='error')

    def test_book_delete(self):
        self.assertTrue(self.library.book_delete(book_id='32336500'))
        self.assertFalse(self.library.book_delete(book_id='0'))

    def test_book_change_status(self):
        self.assertTrue(self.library.book_change_status(book_id='32336500', status='на выдаче'))
        self.assertFalse(self.library.book_change_status(book_id='32336500', status='потеряна'))
        self.assertFalse(self.library.book_change_status(book_id='3233650', status='в наличии'))
        self.assertFalse(self.library.book_change_status(book_id='32336500', status='1'))
        self.assertFalse(self.library.book_change_status(book_id='32336500', status='-1'))
        self.assertFalse(self.library.book_change_status(book_id='32336500', status='0'))
        self.assertFalse(self.library.book_change_status(book_id='0', status='1'))
        self.assertFalse(self.library.book_change_status(book_id='-1', status='1'))
        self.assertFalse(self.library.book_change_status(book_id='dfdf', status='в наличии'))


    def tearDown(self):
        self.session.close()
        os.remove(self.session.name)


if __name__ == "__main__":
  unittest.main()