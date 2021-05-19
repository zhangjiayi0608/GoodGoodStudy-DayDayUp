import unittest
import random


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        print ("setUp for class 1")

    @classmethod
    def setUpClass(cls):
        print ("setUpClass for class 1")

    def test_1(self):
        print ("REALCASE:test_1 for class 1")
        self.assertEqual(True, 1)

    def test_2(self):
        print ("REALCASE:test_2 for class 1")
        assert 1 == 1

    def for_not_test(self):
        print ("REALCASE:for_not_test for class 1")
        assert 1 == 0

    def tearDown(self):
        print ("tearDown for class 1")

    @classmethod
    def tearDownClass(cls):
        print ("tearDownClass for class 1")


class TestDictValueFormatFunctions(unittest.TestCase):
    def setUp(self):
        print('setUp for class 2')
        self.seq = list(range(10))

    def tearDown(self):
        print('tearDown for class 2')

    def test_3(self):
        print('REALCASE:class2:test_3')
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    @unittest.skipIf(6 > 5, "condition is not satisfied!")
    def test_a(self):
        print('REALCASE:class2:test_a')
        self.assertTrue(8 < 10)


if __name__ == '__main__':
    unittest.main()
