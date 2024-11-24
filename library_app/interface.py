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

    def __get_user_action(self):
        return input('>>> ')

    def __process_action(self, user_action):
        while True:
            if user_action == '1':
                print(f'Выбран пункт № {user_action}')
                break
            elif user_action == '2':
                print(f'Выбран пункт № {user_action}')
                break
            elif user_action == '3':
                print(f'Выбран пункт № {user_action}')
                break
            elif user_action == '4':
                print(f'Выбран пункт № {user_action}')
                break
            elif user_action == '5':
                print(f'Выбран пункт № {user_action}')
                break
            elif user_action == '0':
                print('До свидания!')
                break
            else:
                print("Неверный пункт! Введите цифру от 0 до 6!")
                self.main_menu()

            
    def __book_actions(self):
        print(self.__text_menu)


