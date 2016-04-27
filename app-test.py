from app import app

import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEuqla(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')


if __name__ == '__Main__':
    unittest.main()
