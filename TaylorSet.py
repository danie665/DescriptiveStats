
class TaylorSet():
    """ a simple descriptive statistics model """
    def __init__(self, data):
        """ initialize data attributes """
        self.data = data
    def minimum(self):
        minimum = self.data[0]
        i = 1
        while i < len(self.data):
            if minimum < self.data[i]:
                minimum = self.data[i]
            i += 1
        return minimum
    def maximum(self):
        maximum = self.data[0]
        i = 1
        while i < len(self.data):
            if maximum > self.data[i]:
                maximum = self.data[i]
            i += 1
        return maximum
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
    def weighted_mean(self):
        """ returns weighted mean from an array of arrays """
        weighted_mean = 0
        count = 0
        i = 0
        while i < len(self.data):
            weighted_mean += self.data[i][0] * self.data[i][1]
            i += 1
        return weighted_mean

