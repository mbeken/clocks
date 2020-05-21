from django.test import TestCase


class TestClockHandAngle(TestCase):
    def setUp(self):
        self.time = "05:05"
        self.angle = 122.5
        self.client_err_msg1 = "Invalid time format. It should be in 'HH:MM' format."
        self.client_err_msg2 = "Invalid time format. Please input time in 12 hours clock format."
        self.server_err_msg = "Internal Server Error"

    def test_valid_clock_hand_angle(self):
        """
        Success test cases to calculate & return clock hand angle.
        """
        response = self.client.get("/services/clocks/angle/"+self.time)
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response['data']["angle"], self.angle)

        self.time = "12:17"
        self.angle = 93.5
        response = self.client.get("/services/clocks/angle/" + self.time)
        self.assertEqual(response.status_code, 200)
        response = response.json()
        self.assertEqual(response['data']["angle"], self.angle)

    def test_invalid_clock_hand_angle(self):
        """
        Failed test cases to calculate & return clock hand angle.
        """
        self.time = "12:30:30"
        response = self.client.get("/services/clocks/angle/"+self.time)
        self.assertEqual(response.status_code, 400)
        response = response.json()
        self.assertEqual(response['data']["message"], self.client_err_msg1)

        self.time = "12+:-17"
        response = self.client.get("/services/clocks/angle/" + self.time)
        self.assertEqual(response.status_code, 400)
        response = response.json()
        self.assertEqual(response['data']["message"], self.client_err_msg1)

        self.time = "23:10"
        response = self.client.get("/services/clocks/angle/" + self.time)
        self.assertEqual(response.status_code, 400)
        response = response.json()
        self.assertEqual(response['data']["message"], self.client_err_msg2)

