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
        
    def main_menu(self):
        self.__book_actions()
        action = self.__get_user_action()
        self.__process_action(action)

    @staticmethod
    def __get_user_action():
        return input('>>> ')

    def __process_action(self, user_action):
        while True:
            match user_action:
                case '1':
                    print("Список книг:")
                    library_app.book_list()
                    break
                case '2':
                    book_title = input("Введите название книги: ")
                    book_author = input("Введите автора книги: ")
                    book_year = input("Введите год издания книги: ")
                    library_app.book_add(title=book_title, author=book_author, year=book_year)
                    break
                case '3':
                    search_query = input("Введите название, автора или год издания книги: ")
                    library_app.book_search(query=search_query)
                    break
                case '4':
                    book_id = input("Введите ID книги для удаления: ")
                    library_app.book_delete(book_id=book_id)
                    break
                case '5':
                    book_id = input("Введите ID книги: ")
                    book_status = input("Введите новый статус (в наличии или выдана): ")
                    library_app.book_change_status(book_id=book_id, status=book_status)
                    break
                case '0':
                    print('До свидания!')
                    raise SystemExit
                case _:
                    print("Неверный пункт! Введите цифру от 0 до 6!")
                    self.main_menu()

            
    def __book_actions(self):
        print(self.__text_menu)


