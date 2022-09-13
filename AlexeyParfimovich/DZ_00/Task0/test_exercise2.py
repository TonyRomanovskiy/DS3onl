import unittest
import exercise2 as unit

class Test_exercise2(unittest.TestCase):

    def test_Celsius2Fahrenheit(self):
        self.assertEqual(unit.Celsius2Fahrenheit(float([-10.0, -5.0, 0.0, 5.0, 10.0])), [16.0, 27.0, 32.0, 41.0, 50.0])

if __name__ == '__main__':
    unittest.main()
