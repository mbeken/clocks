import unittest
from clock_find import calc_angle, app

class Test(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

    def test_clock_negative_testing(self):
        data=calc_angle(26,30)
        expected_data= "Invalid hour given"
        self.assertEqual(expected_data,data)

        data=calc_angle(12,67)
        expected_data = "Minute should be in range of  0 to 59"
        self.assertEqual(expected_data, data)

        data = calc_angle(-2, 67)
        expected_data = "Minute should be in range of  0 to 59"
        self.assertEqual(expected_data, data)

        data = calc_angle(-2, -67)
        expected_data = "Minute should be in range of  0 to 59"
        self.assertEqual(expected_data, data)

    def test_clock_positive_testing(self):
        data=calc_angle(2,20)
        expected_data= 50
        self.assertEqual(expected_data, data)

        data=calc_angle(22,20)
        expected_data= 170
        self.assertEqual(expected_data, data)

if __name__ == "__main__":
    unittest.main()

