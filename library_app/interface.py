from .library import LibraryApp


library_app = LibraryApp()

class LibraryInterface:
    def __init__(self):
        self.__user_action = None

        self.__text_menu = ("Добро пожаловать в библиотеку!\n"
                     "Введите нужный пункт меню. (Цифра от 0 до 5)\n"
                     "1. Посмотреть все книги\n"
                     "2. Добавить книгу\n"
                     "3. Найти книгу\n"
                     "4. Удалить книгу\n"
                     "5. Изменить статус книги\n"
                     "___________________________________\n"
                     "0. Выйти из программы")

        self.__text_search = ("По какому параметру искать книги?\n"
                            "Введите нужный пункт меню. (Цифра от 1 до 3)\n"
                            "Для выхода из меню поиска введите 0\n"
                            "1. Поиск по названию\n"
                            "2. Поиск по автору\n"
                            "3. Поиск по году издания\n"
                            "___________________________________\n"
                            "0. Выйти из меню поиска")

        self.__text_book_status = ("Выберите новый статус:\n"
                              "1. В наличии\n"
                              "2. На выдаче\n"
                              "Для выхода введите 0\n")

    def print_main_menu(self):
        print(self.__text_menu)
        action = self.__get_user_action()
        self.__process_main_menu(action)

    def print_back_message(self):
        print("\nВведите 0 для возврата в главное меню")
        action = self.__get_user_action()
        match action:
            case '0':
                self.print_main_menu()
            case _:
                self.print_back_message()

    def print_search_menu(self):
        print(self.__text_search)
        action = self.__get_user_action()
        self.__process_search(action)

    def print_change_book_status_menu(self, book_id: str):
        print(self.__text_book_status)
        action = self.__get_user_action()
        self.__process_change_status(action, book_id=book_id)

    @staticmethod
    def __get_user_action():
        return input('>>> ')

    def __print_books(self, books: dict) -> None:
        for book in books:
            print(f'ID - {book}')
            print(f'Автор - {books[book]["author"]}')
            print(f'Название - {books[book]["title"]}')
            print(f'Год издания - {books[book]["year"]}')
            print(f'Статус - {books[book]["status"]}')
            print('---------------------------------------')

    def __process_main_menu(self, user_action):
        while True:
            match user_action:
                case '1':
                    books = library_app.book_list()
                    if books:
                        print("Список книг:")
                        self.__print_books(books)
                        self.print_back_message()
                    else:
                        print('Нет доступных книг')
                        self.print_back_message()
                case '2':
                    book_title = input("Введите название книги: ")
                    book_author = input("Введите автора книги: ")
                    book_year = input("Введите год издания книги: ")
                    library_app.book_add(title=book_title, author=book_author, year=book_year)
                    self.print_back_message()
                case '3':
                    self.print_search_menu()
                case '4':
                    print('Введите ID книги для удаления или 0 для выхода')
                    book_id = input(">>> ")
                    if book_id == '0':
                        self.print_main_menu()
                    if library_app.book_delete(book_id=book_id):
                        print(f'Книга с ID {book_id} удалена!')

                case '5':
                    book_id = input("Введите ID книги или exit для выхода: ")
                    book_status = library_app.get_book_status(book_id)
                    if book_id.lower() == 'exit':
                        self.print_main_menu()
                    if book_status:
                        print(f'Текущий статус книги - {book_status}')
                        self.print_change_book_status_menu(book_id)
                case '0':
                    print('До свидания!')
                    raise SystemExit
                case _:
                    print("Неверный пункт! Введите цифру от 0 до 6!")
                    self.print_main_menu()

    def __process_search(self, user_action):
        while True:
            match user_action:
                case '1':
                    title = input("Введите название книги: ")
                    books = library_app.book_search_title(title)
                    if books:
                        self.__print_books(books)
                        self.print_back_message()
                    else:
                        print('Нет доступных книг')
                        self.print_back_message()
                case '2':
                    author = input("Введите автора книги: ")
                    books = library_app.book_search_author(author)
                    if books:
                        self.__print_books(books)
                        self.print_back_message()
                    else:
                        print('Нет доступных книг')
                        self.print_back_message()
                case '3':
                    year = input("Введите год издания книги: ")
                    books = library_app.book_search_year(year)
                    if books:
                        self.__print_books(books)
                        self.print_back_message()
                    else:
                        print('Нет доступных книг')
                        self.print_back_message()
                case '0':
                    self.print_main_menu()
                case _:
                    print("Неверный пункт! Введите цифру от 0 до 6!")
                    self.print_search_menu()

    def __process_change_status(self, user_action: str, book_id: str):
        match user_action:
            case '1':
                book_status = 'В наличии'
                result = library_app.book_change_status(book_id=book_id, status=book_status)
                if result:
                    print('Статус книги успешно изменен')
                    self.print_back_message()
                else:
                    self.print_change_book_status_menu(book_id)
            case '2':
                book_status = 'На выдаче'
                result = library_app.book_change_status(book_id=book_id, status=book_status)
                if result:
                    print('Статус книги успешно изменен')
                    self.print_back_message()
                else:
                    self.print_change_book_status_menu(book_id)
            case '0':
                self.print_main_menu()
            case _:
                print("Неверный пункт!")
                self.print_change_book_status_menu(book_id)

