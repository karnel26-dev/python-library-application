from library_app import LibraryApp, LibraryDB, LibraryInterface


def main():
    db = LibraryDB('books.json')
    session = db.session_maker()

    interface = LibraryInterface()
    interface.main_menu()


if __name__ == '__main__':
    main()