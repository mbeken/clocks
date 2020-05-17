import unittest
import main_old


class TestClock(unittest.TestCase):
    def test_case(self):
        time="3:0"
        result=main_old.trigger_function(time)
        self.assertEqual(result,90)

unittest.main()




