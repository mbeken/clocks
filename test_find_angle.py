import unittest

from find_angle import app, get_clock_angle


class testClock(unittest.TestCase):

    def setUp(self):
        # self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def test_get_clock_angle_for_time_fail_testing(self):
        """Test case for fail testing """
        data = get_clock_angle("as:aa")
        expected_data = "Please enter the valid format i.e. This time function will accept time b/w 00:00 To 23:59."
        self.assertEqual(expected_data, data.json['context'])

        data = get_clock_angle("as:11")
        expected_data = "Please enter the valid format i.e. This time function will accept time b/w 00:00 To 23:59."
        self.assertEqual(expected_data, data.json['context'])

        data = get_clock_angle("111:12")
        expected_data = "Please enter the valid format i.e. This time function will accept time b/w 00:00 To 23:59."
        self.assertEqual(expected_data, data.json['context'])

        data = get_clock_angle("24:60")
        expected_data = "Please enter the valid format i.e. This time function will accept time b/w 00:00 To 23:59."
        self.assertEqual(expected_data, data.json['context'])

    def test_get_clock_angle_for_time_pass_testing(self):
        """Test case for pass testing  """
        data = get_clock_angle("00:59")
        expected_data = "Angle for time 00:59 is 35.5 degree."
        self.assertEqual(expected_data, data.json['context'])

        data = get_clock_angle("12:59")
        expected_data = "Angle for time 12:59 is 35.5 degree."
        self.assertEqual(expected_data, data.json['context'])

        data = get_clock_angle("01:00")
        expected_data = "Angle for time 01:00 is 30.0 degree."
        self.assertEqual(expected_data, data.json['context'])

        data = get_clock_angle("03:20")
        expected_data = "Angle for time 03:20 is 20.0 degree."
        self.assertEqual(expected_data, data.json['context'])


if __name__ == '__main__':
    unittest.find_angle()
