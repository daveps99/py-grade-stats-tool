import sqlite3
from sqlite3 import Error

class Connection():
    '''
    SQLite database connector
    '''

    def __init__(self):
        self.connection = None

    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Successful connection to the database")
        except Error as e:
            return "Database already created"

        return connection

connection = Connection().create_connection("students.db")

