import os.path


class LibraryDB:
    def __init__(self, db_name):
        if os.path.exists(db_name):
            self.db_file = open(db_name, 'r+')
        else:
            self.db_file = open(db_name, 'w')

    def session_maker(self):
        return self.db_file

