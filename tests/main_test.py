import unittest

from main import app, return_angle, check_valid_time

class TestClocks(unittest.TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def test_return_angle(self):
        """Test cases for return_angle function"""

        response = return_angle("03:00").get_json()
        expected_response = {'response': 90}

        exception_response = return_angle("24:00").get_json()
        expected_exception_response = {'response': 'The format for time is not valid, '
                                                              'format should be of type "03:00"'}

        self.assertEqual(response['response'], expected_response['response'])
        self.assertEqual(exception_response['response'], expected_exception_response['response'])

    def test_check_valid_time(self):
        """Test case for check_valid_time function"""
        valid_response = check_valid_time("04:00")
        invalid_response = check_valid_time("24:00")

        self.assertTrue(valid_response)
        self.assertFalse(invalid_response)


if __name__ == "__main__":
    unittest.main()

