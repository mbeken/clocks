import unittest
from clock_utils import send_angle, find_hour_and_minute_angle

class TestSendAngle(unittest.TestCase):

    def test_send_angle(self):
        data = send_angle("10:10")
        self.assertEqual(data["angle"], 245.0)

    def test_send_angle_acute(self):
        data = send_angle("23:59")
        self.assertEqual(data["angle"],5.5)

    def test_send_angle_negative(self):
        data = send_angle("-23:59")
        self.assertEqual(data["err_msg"],"Enter valid colon separated time string")

    def test_send_angle_invalid(self):
        data = send_angle("ASQW")
        self.assertRaises(ValueError)
        self.assertEqual(data["err_msg"], "Enter valid colon separated time string")

    def test_hour_and_minute_angle(self):
        hour_angle, minute_angle = find_hour_and_minute_angle(11,59)
        self.assertEqual(hour_angle,359.5)
        self.assertEqual(minute_angle, 354.0)