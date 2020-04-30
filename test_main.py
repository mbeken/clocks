import unittest

from main import clock_angle_between_hands_m

class testclock(unittest.TestCase):
    def test_clock_h6m0(self):
        self.assertEqual(clock_angle_between_hands_m(6,0), 180.0)

if __name__ == '__main__':
    unittest.main()