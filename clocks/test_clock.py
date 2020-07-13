import unittest
from clocks.views import calc_angle

class Test(unittest.TestCase):

    def test_calc_angle_negative(self):

        data=calc_angle("26:30")
        expected_data= "Invalid hour given"
        self.assertEqual(expected_data,data)

        data=calc_angle("12:67")
        expected_data = "Minute should be in range of  0 to 59"
        self.assertEqual(expected_data, data)

        data = calc_angle("-2:67")
        expected_data = "Minute should be in range of  0 to 59"
        self.assertEqual(expected_data, data)

        data = calc_angle("-2:-67")
        expected_data = "Minute should be in range of  0 to 59"
        self.assertEqual(expected_data, data)

    def test_calc_angle_positive(self):
        data = calc_angle("22:20")
        expected_data = "Angle for time is 170.0 degree."
        self.assertEqual(expected_data, data)





