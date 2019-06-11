import unittest
from DescriptiveStats import DescriptiveStats

class ConvertToFloatFailures(unittest.TestCase):
    @unittest.expectedFailure
    def test_strings_convert(self):
        # ensure string to float converion fails
        my_data = [ "One", "Two", "Three" ]
        my_set = DescriptiveStats(data_1=my_data)

class BuiltIns(unittest.TestCase):
    def test_minimum(self):
        my_data = [ 10, 20, 12, 17, 16 ]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertEqual(min(my_set.data_1), 10)
    def test_maximum(self):
        my_data = [ 10, 20, 12, 17, 16 ]
        my_set = DescriptiveStats(my_data)
        self.assertEqual(max(my_set.data_1), 20)

class Center(unittest.TestCase):
    def test_mean(self):
        my_data = [ 10, 20, 12, 17, 16 ]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertEqual(my_set.mean(my_set.data_1), 15)
    def test_median_odd(self):
        my_data = [ 10, 20, 12, 17, 16 ]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertEqual(my_set.median(my_set.data_1), 16)
    def test_median_even(self):
        my_data = [ 10, 20, 12, 17, 16, 14 ]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertEqual(my_set.median(my_set.data_1), 15)
    def test_geometic_mean(self):
        my_data = [ 1.10, 1.15, 1.21, 0.51, 1.05 ]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertAlmostEqual(my_set.geometric_mean(my_set.data_1), .9610, 4)
    def test_easy_mode(self):
        my_data = [ 1, 1, 2, 3 ]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertEqual(my_set.mode(my_set.data_1), 1)
    def test_hard_mode(self):
        my_data = [ 1, 1, 2, 2, 3 ]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertEqual(my_set.mode(my_set.data_1), [ 1, 2 ])

class Dispersion(unittest.TestCase):
    def test_range(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(my_data)
        self.assertEqual(my_set.range(my_set.data_1), 10)
    def test_population_variance(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(my_data)
        self.assertEqual(my_set.population_variance(my_set.data_1), 12.8)
    def test_sample_variance(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(my_data)
        self.assertEqual(my_set.sample_variance(my_set.data_1), 16)
    def test_population_standard_deviation(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(my_data)
        self.assertAlmostEqual(my_set.population_standard_deviation(my_set.data_1), 3.5777, 4)
    def test_sample_standard_deviation(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertEqual(my_set.sample_standard_deviation(my_set.data_1), 4)
    def test_population_coefficient_of_variation(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertAlmostEqual(
                my_set.population_coefficient_of_variation(my_set.data_1), .2385, 4)
    def test_sample_coefficient_of_variation(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertAlmostEqual(my_set.sample_coefficient_of_variation(my_set.data_1), .2667, 4)
    def test_percentile(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertEqual(my_set.percentile(.25, data=my_set.data_1), 11)
    def test_interquartile_range(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertEqual(my_set.interquartile_range(my_set.data_1), 7.5)

class ZScore(unittest.TestCase):
    def test_population_z_score(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertAlmostEqual(my_set.population_z_score(0, data=my_set.data_1), -1.3975, 4)
    def test_sample_z_score(self):
        my_data = [10, 20, 12, 17, 16]
        my_set = DescriptiveStats(data_1=my_data)
        self.assertEqual(my_set.sample_z_score(0, data=my_set.data_1), -1.25)

class Covariance(unittest.TestCase):
    def test_sample_covariance(self):
        my_data_1 = [2, 5, 1, 3, 4, 1, 5, 3, 4, 2]
        my_data_2 = [50, 57, 41, 54, 54, 38, 63, 48, 59, 46]
        my_set = DescriptiveStats(data_1=my_data_1, data_2=my_data_2)
        self.assertEqual(my_set.sample_covariance(my_set.data_1, my_set.data_2), 11)
    def test_population_covariance(self):
        my_data_1 = [2, 5, 1, 3, 4, 1, 5, 3, 4, 2]
        my_data_2 = [50, 57, 41, 54, 54, 38, 63, 48, 59, 46]
        my_set = DescriptiveStats(data_1=my_data_1, data_2=my_data_2)
        self.assertEqual(my_set.population_covariance(my_set.data_1, my_set.data_2), 9.9)

unittest.main()
