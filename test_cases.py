# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:08:37 2020

@author: arawal
Function to unitesting of http function
"""



import os
import sys
import unittest

from unittest.mock import Mock
from flask import Flask

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import main


app = Flask(__name__)

class MyTestClass(unittest.TestCase):
    """
    Class to implment TestCases for Clock Angle function in main
    """
    # initialization logic for the test suite declared in the test module
    # code that is executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        pass

    # clean up logic for the test suite declared in the test module
    # code that is executed after all tests in one test run
    @classmethod
    def tearDownClass(cls):
        pass

    # initialization logic
    # code that is executed before each test
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    # clean up logic
    # code that is executed after each test
    def tearDown(self):
        pass

     # Tesing angle between the codes
    def test_h3m0(self):
        """
        Testing at 3 hrs 0 mins - Angle = 90
        """
        hrs = 3
        mins = 0
        data = {'hrs': hrs, 'mins': mins}
        req = Mock(get_json=Mock(return_value=data), args=data)

        # Call tested function
        angle1 = float(main.clock_angle(req).split('Angle ->')[1])
        self.assertEqual(angle1, 90.0)

    def test_2m45(self):
        """
        Testing at 2 hrs 45 mins - Angle = 187.5
        """
        hrs = 2
        mins = 45
        data = {'hrs': hrs, 'mins': mins}
        req = Mock(get_json=Mock(return_value=data), args=data)

        # Call tested function
        angle1 = float(main.clock_angle(req).split('Angle ->')[1])
        self.assertEqual(angle1, 187.5)

    def test_h8m15(self):
        """
        Testing at 8 hrs 15 mins - Angle = 157.5
        """
        hrs = 8
        mins = 15
        data = {'hrs': hrs, 'mins': mins}
        req = Mock(get_json=Mock(return_value=data), args=data)

        # Call tested function
        angle1 = float(main.clock_angle(req).split('Angle ->')[1])
        self.assertEqual(angle1, 157.5)

    def test_h6m0(self):
        """
        Testing at 6 hrs 0 mins - Angle = 180
        """
        hrs = 6
        mins = 0
        data = {'hrs': hrs, 'mins': mins}
        req = Mock(get_json=Mock(return_value=data), args=data)

        # Call tested function
        angle1 = float(main.clock_angle(req).split('Angle ->')[1])
        self.assertEqual(angle1, 180)


# runs the unit tests in the module
if __name__ == '__main__':
    unittest.main()
