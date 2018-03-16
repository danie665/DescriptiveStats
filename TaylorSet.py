class TaylorSet():
    """ a simple descriptive statistics model """
    def __init__(self, data):
        """ initialize data """
        self.data = data
        self.data = [float(x) for x in self.data]
        self.data.sort()
    def mean(self):
        """ returns the arithmetic mean of an array """
        return sum(self.data) / len(self.data)
    def median(self):
        """ returns the median of an array """
        place = len(self.data) / 2
        return(place)
    def range(self):
        """ return the range of the data """
        return 0
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
