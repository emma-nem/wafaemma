import unittest
import MyMathLib
    
class DivisionTest(unittest.TestCase):
    def testSumPositiveNumbersOneAndOne(self):
        division = MyMathLib.Division()
        self.assertEqual(1,division.execute(1,1))

    def testSumPositiveNumbersOneAndTwo(self):
        division = MyMathLib.Division()
        self.assertEqual(3,division.execute(6,2))

    def testSumPositiveNumbersTwoAndTwo(self):
        division = MyMathLib.Division()
        self.assertEqual(4,division.execute(8,2))

    def testSumZero(self):
        division = MyMathLib.Division()
        self.assertEqual(0,division.execute(0,1))

    def testSumNegativeNumbers(self):
        division = MyMathLib.Division()
        self.assertEqual(-2,division.execute(-2,1))

if __name__ == '__main__':
    unittest.main()