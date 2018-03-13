import unittest

from TaylorSet import TaylorSet

class MeanAndMedian(unittest.TestCase):
    def method_one_mean(self):
        my_data = [ 10, 20, 12, 17, 16 ]
        my_set = TaylorSet(my_data)
        self.assertEqual(my_set.mean(), 15)
    def method_one_median(self):
        my_data = [ 10, 20, 12, 17, 16 ]
        my_set = TaylorSet(my_data)
        self.assertEqual(myset
unittest.main()
