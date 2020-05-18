"""Unit test
"""
# coding: utf-8

# In[14]:

import unittest
class Testing(unittest.TestCase):
    def test_1(self):
        try:
            hour = int(3)
            minute = int(0)
            if ((hour >= 1) & (hour <= 12)) & ((minute >= 0) & (minute <= 60)):
                angle = abs((hour * 30 + minute * 0.5)-(minute * 6))
            else:
                angle = "Enter correct interger value"
        except ValueError:
            angle = "Enter correct interger value"
        self.assertEqual(angle, 90)
    def test_3(self):
        hour = 13
        minute = 50
        try:
            if ((hour >= 1) & (hour <= 12)) & ((minute >= 0) & (minute <= 60)):
                angle = abs((hour * 30 + minute * 0.5)-(minute * 6))
            else:
                angle = "Enter correct interger value"
        except ValueError:
            angle = "Enter correct interger value"
        self.assertEqual(angle, "Enter correct interger value")
if __name__ == '__main__': 
    unittest.main()
    