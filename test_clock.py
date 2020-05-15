import unittest
from clock import Clock_Angle

class TestClock(unittest.TestCase):
    
    def test_check_angle(self):
        ca= Clock_Angle(3,0)
        angle= ca.checkValues()
        self.assertEqual(angle,90, "Angle is 90")
    
    def test_check_range(self):
        ca= Clock_Angle(23213,4324)
        result= ca.checkValues()
        self.assertEqual(result,"Incorrect hour and minutes value", "incorrect values" )

if __name__ == '__main__':
    unittest.main()