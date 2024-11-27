from library_app import LibraryApp, LibraryInterface
from library_app.db import Session

def main():
    session = Session.session_maker()

    library = LibraryApp(session)

    interface = LibraryInterface(library)
    interface.print_main_menu()


if __name__ == '__main__':
    main()