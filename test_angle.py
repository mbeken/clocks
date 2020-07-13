import unittest

from angle import app, find_angle
from flask import request

class TestClocks(unittest.TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def test_find_angle_pass(self):
        """Test cases for find_angle function"""
        data = find_angle("05:30").get_json()
        #print("the the ", data)
        expected_data = {"angle": 15.0}
        self.assertEqual(expected_data['angle'], data['angle'])

        data = find_angle("12:59").get_json()
        expected_data ={"angle": 35.5}
        self.assertEqual(expected_data['angle'], data['angle'])

    def test_find_angle_fail(self):
        """Test cases for find_angle function"""
        data = find_angle("46:889").get_json()
        #print("the the ", data)
        expected_data = {'angle':'Time is not in required format from 00:00 to 23:59'}
        self.assertEqual(expected_data['angle'], data['angle'])

        data = find_angle("36:888").get_json()
        expected_data ={'angle':'Time is not in required format from 00:00 to 23:59'}
        self.assertEqual(expected_data['angle'], data['angle'])

if __name__ == "__main__":
    unittest.main()
