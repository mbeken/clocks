from unittest import TestCase

import pytest

from clockAngle import ClockAngleCalculator


class TestClockAngleCalculator(TestCase):

    def test_input_validation(self):
        obj = ClockAngleCalculator
        with pytest.raises(Exception, match=r"Input validation failed, Please use specified format *"):
            assert obj.input_validation(self, input_time="33:00:00")

    def test_clock_angle(self):
        obj = ClockAngleCalculator
        time = "03:00:00"
        extracted_time = obj.input_validation(self, input_time=time)
        self.assertEqual(obj.clock_angle(self, time=extracted_time), 90.0)


if __name__ == '__main__':
    TestCase.main()
