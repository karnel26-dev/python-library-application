import os
import json


class LibraryDB:
    """

    """
    def __init__(self, db_name):
        if os.path.exists(db_name):
            self.db_file = open(db_name, 'r+')

        else:
            self.db_file = open(db_name, 'w+')

            initial_data = {'library':
                                {
                                    'books':
                                        {}
                                }}

            json.dump(initial_data, self.db_file, indent=2)

    def session_maker(self):
        return self.db_file


Session = LibraryDB(db_name='books.json')

