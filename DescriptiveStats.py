class DescriptiveStats():

    """ a simple descriptive statistics model """

    def __init__(self, data, data_2=[], data_3=[], data_4=[], data_5=[]):
        """ initialize data """
        self.data = data
        self.data = [float(x) for x in self.data]
        self.data_2 = data_2
        self.data_2 = [float(x) for x in self.data_2]
        self.data_3 = data_3
        self.data_3 = [float(x) for x in self.data_3]
        self.data_4 = data_4
        self.data_4 = [float(x) for x in self.data_4]
        self.data_5 = data_5
        self.data_5 = [float(x) for x in self.data_5]

    def _lists_uniform(self):
        """ ensures that both input lists are the same length """
        length = len(data)
        if (
                (len(data_2) == length or len(data_2) == 0) and
                (len(data_3) == length or len(data_3) == 0) and
                (len(data_4) == length or len(data_4) == 0) and
                (len(data_5) == length or len(data_5) == 0)
            ):
            return True
        return False

    def mean(self):
        """ returns the arithmetic mean of an array """
        return sum(self.data) / len(self.data)

    def median(self):
        """ returns the median of an array """
        sorted_array = sorted(self.data)
        if len(sorted_array) % 2 == 0:
            lower = int( ( len(sorted_array) / 2 ) )
            upper = int( ( len(sorted_array) / 2 ) + 1 )
            return ( sorted_array[lower-1] + sorted_array[upper-1] ) / 2
        else:
            place = int( ( len(sorted_array) + 1 ) / 2 )
            return sorted_array[place-1]

    def mode(self):
        """ return the mode of the data """
        tally_dict = {}
        i = 0
        while i < len(self.data):
            if self.data[i] in tally_dict:
                tally_dict[self.data[i]] += 1
            else:
                tally_dict[self.data[i]] = 1
            i += 1
        max_occ = 0
        for key, value in tally_dict.items():
            if value > max_occ:
                max_occ = value
        modes = []
        for key, value in tally_dict.items():
            if value == max_occ:
                modes.append(key)
        if len(modes) == 1:
            return modes[0]
        else:
            return modes

    def range(self):
        """ return the range of the data """
        return max(self.data) - min(self.data)

    def weighted_mean(self):
        """ returns weighted mean from an array of arrays """
        if not _lists_uniform():
            raise ValueError
        return 0

    def geometric_mean(self):
        """ returns geometic mean of an array """
        my_product = 1
        i = 0
        while i < len(self.data):
            my_product *= self.data[i]
            i += 1
        return my_product ** ( 1 / len(self.data) )

    def percentile(self, percentile):
        """ returns the percentile location of an array """
        sorted_array = sorted(self.data)
        location = ( len(sorted_array) + 1 ) * percentile
        lower = int(location) - 1
        upper = int(location)
        mid_distance = location - int(location)
        return ( sorted_array[lower] +
                (( sorted_array[upper] - sorted_array[lower] ) * mid_distance ) )

    def interquartile_range(self):
        """ returns the interquartile range of an array """
        return self.percentile(.75) - self.percentile(.25)

    def population_variance(self):
        """ returns population variance of an array """
        my_mean = self.mean()
        my_sum = 0
        i = 0
        while i < len(self.data):
            my_sum += ( self.data[i] - my_mean ) ** 2
            i += 1
        return my_sum / len(self.data)

    def sample_variance(self):
        """ returns sample variance of an array """
        my_mean = self.mean()
        my_sum = 0
        i = 0
        while i < len(self.data):
            my_sum += ( self.data[i] - my_mean ) ** 2
            i += 1
        return my_sum / ( len(self.data) - 1 )

    def population_standard_deviation(self):
        """ returns the population standard deviation of an array """
        return self.population_variance() ** 0.5

    def sample_standard_deviation(self):
        """ returns the sample standard deviation of an array """
        return self.sample_variance() ** 0.5

    def population_coefficient_of_variation(self):
        """ returns the population coefficient of variation of an array """
        return self.population_standard_deviation() / self.mean()

    def sample_coefficient_of_variation(self):
        """ returns the sample coefficient of variation of an array """
        return self.sample_standard_deviation() / self.mean()

    def population_z_score(self, position):
        """ returns the population z-score of an element in an array """
        return ( self.data[position] - self.mean() ) / self.population_standard_deviation()

    def sample_z_score(self, position):
        """ returns the sample z-score or an element in a list """
        return ( self.data[position] - self.mean() ) / self.sample_standard_deviation()

    def sample_covariance(self):
        """ returns the sample covariance of an array """
        i = 0
        while (i < 
        return 0

    def population_covariance(self):
        """ returns the population covariance of an array """
        return 0
