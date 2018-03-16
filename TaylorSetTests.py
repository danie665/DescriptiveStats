import unittest
from TaylorSet import TaylorSet

class ConvertToFloatFailures(unittest.TestCase):
    @unittest.expectedFailure
    def test_strings_convert(self):
        # ensure string to float converion fails
        my_data = [ "One", "Two", "Three" ]
        my_set = TaylorSet(my_data)

class BuiltIns(unittest.TestCase):
    def test_minimum(self):
        my_data = [ 10, 20, 12, 17, 16 ]
        my_set = TaylorSet(my_data)
        self.assertEqual(min(my_set.data), 10)
    def test_maximum(self):
        my_data = [ 10, 20, 12, 17, 16 ]
        my_set = TaylorSet(my_data)
        self.assertEqual(max(my_set.data), 20)

class Center(unittest.TestCase):
    def test_mean(self):
        my_data = [ 10, 20, 12, 17, 16 ]
        my_set = TaylorSet(my_data)
        self.assertEqual(my_set.mean(), 15)
    def test_median(self):
        my_data = [ 10, 20, 12, 17, 16 ]
        my_set = TaylorSet(my_data)
        print(my_set.median())


unittest.main()
