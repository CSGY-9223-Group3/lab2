import unittest
from app import get_data


class TestApp(unittest.TestCase):
    def test_get_data(self):
        response = get_data()
        expected_data = {"message": "Hello, World!", "status": "success"}
        # Since get_data uses jsonify, it returns a Response object
        # We need to get the JSON data from the response
        self.assertEqual(response.get_json(), expected_data)


if __name__ == "__main__":
    unittest.main()
