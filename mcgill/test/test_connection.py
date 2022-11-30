import sys
from mcgill.src.db.sql_connect import Connection
import unittest

class ConnectionTest(unittest.TestCase):
    
    def setUp(self) -> None:
        self.connection = Connection()

    def test_connection(self):
        path = "../src/db/students.db"
        connected = self.connection.create_connection(path)

        self.assertIsNotNone(connected)
