import unittest
import MyMathLib
    
class AddTest(unittest.TestCase):
    def testSumPositiveNumbersOneAndOne(self):
        add = MyMathLib.Add()
        self.assertEqual(2,add.execute(1,1))

    def testSumPositiveNumbersOneAndTwo(self):
        add = MyMathLib.Add()
        self.assertEqual(3,add.execute(1,2))

    def testSumPositiveNumbersTwoAndTwo(self):
        add = MyMathLib.Add()
        self.assertEqual(4,add.execute(2,2))

    def testSumZero(self):
        add = MyMathLib.Add()
        self.assertEqual(1,add.execute(0,1))

    def testSumNegativeNumbers(self):
        add = MyMathLib.Add()
        self.assertEqual(-1,add.execute(-2,1))

if __name__ == '__main__':
    unittest.main()