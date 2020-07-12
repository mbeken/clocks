import unittest
from mock import patch, MagicMock
import pytest
import datetime
from ClockAngleCalculator import ClockAngleCalculator

class TestClockAngleCalculator(unittest.TestCase):

    def setUp(self):
        self.obj = ClockAngleCalculator()

    def test_input_validation(self):
        with pytest.raises(Exception, match=r"Input validation failed, Please use specified format *"):
            assert self.obj.input_validation(input_time="33:00:00")

    def test_clock_angle(self):

        self.assertEqual(self.obj.clock_angle(time=datetime.datetime.strptime("03:00:00", "%H:%M:%S")), 90.0)

suite = unittest.TestLoader().loadTestsFromTestCase(TestClockAngleCalculator)
unittest.TextTestRunner(verbosity=2).run(suite)
