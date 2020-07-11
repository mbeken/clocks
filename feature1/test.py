import unittest
import main


class TestMain(unittest.TestCase):
    def test_case_1(self):
        time_value = "03:00"
        result = main.getAngles(time_value)
        self.assertEqual(result, 90)


unittest.main()