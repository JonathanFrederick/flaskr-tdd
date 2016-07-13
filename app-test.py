import app
import os
import unittest
import tempfile
import psycopg2
import re
from app import name_from_uri, connect_db


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        # conn = psycopg2.connect(database='flaskr_tdd')
        cursor = connect_db()
        # TODO: figure out a better string of sql commands
        cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
        self.assertIsInstance(cursor.fetchall(), list)


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a blank test database before each test"""
        self.db_name = name_from_uri(os.environ['TEST_DATABASE_URL'])
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        app.init_db(self.db_name)

    def tearDown(self):
        """Destroy test database after each test"""
        app.drop_db(self.db_name)

    def login(self, username, password):
        """Login helper function"""
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        """Logout helper function"""
        return self.app.get('/logout', follow_redirects=True)

    def test_empty_db(self):
        """Ensure database is blank"""
        rv = self.app.get('/')
        assert b'<em>No entries here so far</em>' in rv.data
        assert b'<ul class="entries">\n    <li><h2>' not in rv.data




if __name__ == '__main__':
    unittest.main()
