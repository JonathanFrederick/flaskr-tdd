from app import app
import os
import unittest
import psycopg2


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_database(self):
        conn = psycopg2.connect(database='flaskr_tdd')
        cursor = conn.cursor()
        cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        self.assertTrue(cursor.fetchall())



if __name__ == '__main__':
    unittest.main()
