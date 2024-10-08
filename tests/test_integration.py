import unittest
from app import app


class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        # Propagate the exceptions to the test client
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), 'Welcome to the Flask App!')

    def test_api_data(self):
        response = self.app.get('/api/data')
        expected_data = {
            'message': 'Hello, World!',
            'status': 'success'
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), expected_data)



if __name__ == '__main__':
    unittest.main()
