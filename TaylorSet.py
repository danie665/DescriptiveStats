
class TaylorSet():
    """ a simple descriptive statistics model """
    def __init__(self, data):
        """ initialize data attributes """
        self.data = data
    def minimum(self):
        """ returns the minimum value of an array """
        minimum = self.data[0]
        i = 1
        while i < len(self.data):
            if minimum < self.data[i]:
                minimum = self.data[i]
            i += 1
        return minimum
    def maximum(self):
        """ returns the maximum value of an array """
        maximum = self.data[0]
        i = 1
        while i < len(self.data):
            if maximum > self.data[i]:
                maximum = self.data[i]
            i += 1
        return maximum
    def median(self):
        """ returns the median from an array """
        temp_array = self.data
        sorted_array
        half = (len(self.data) + 1)
        if half % 2 == 0:
            index = half / 2 
            return self.data[index]
        else:
            lower_index = (half / 2) - .5
            upper_index = (half / 2) + .5
            average = (self.data[upper_index] + self.data[lower_index]) / 2 
            return average
    def range(self):
        """ return the range of the data """
        return 0
    def mean(self):
        """ returns mean from an array """
        count = 0
        total = 0
        i = 0
        while i < len(self.data):
            count += 1
            total += self.data[i]
            i += 1
        return total / count
    def weighted_mean(self):
        """ returns weighted mean from an array of arrays """
        weighted_mean = 0
        count = 0
        i = 0
        while i < len(self.data):
            weighted_mean += self.data[i][0] * self.data[i][1]
            i += 1
        return weighted_mean
    def geometic_mean(self):
        """ returns geometic mean of an array """
        return 0
    def percentile_location(self):
        """ returns the percentile location of an array """
        return 0
    def interquartile_range(self):
        """ returns the interquartile range of an array """
        return 0
    def population_variance(self):
        """ returns population variance of an array """
        return 0
    def sample_variance(self):
        """ returns sample variance of an array """
        return 0
    def standard_deviation(self):
        """ returns the standard deviation of an array """
        return 0
    def coefficient_of_variation(self):
        """ returns the coefficient of variation of an array """
        return 0
    def z_score(self):
        """ returns the z-score of an element in an array """
        return 0
    def sample_covariance(self):
        """ returns the sample covariance of an array """
        return 0
    def population_covariance(self):
        """ returns the population covariance of an array """
        return 0
    def pearson_sample(self):
        """ returns the pearson product moment correlation coefficient for sample data """
        return 0
    def pearson_population(self):
        """ returns the pearson product moment correlation coefficient for population data """
        return 0
