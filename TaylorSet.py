
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
        maximum = self.data [0]
        i = 1
        while i < len(self.data):
            if maximum > self.data[i]:
                maximum = self.data[i]
            i += 1
        return maximum
    def average(self):
        count = 0
        total = 0
        i = 0
        while i < len(self.data):
            count += 1
            total += self.data[i]
            i += 1
        return total / count

