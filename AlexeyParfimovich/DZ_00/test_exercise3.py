import unittest
import exercise3 as unit

class Test_exercise3(unittest.TestCase):

    def test_getUniqueElements(self):
        self.assertEqual(unit.getUniqueElements([1,2,3,1,3,3,1,2,3]), [1,2,3])

if __name__ == '__main__':
    unittest.main()
