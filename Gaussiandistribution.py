import math
import matplotlib.pyplot as plt
from .Generaldistribution import distribution

class Gaussian(Distribution):
    """ Gaussian distribution class for calculating and
    visualizing a Gaussian distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file

    """
    def __init__(self, mu = 0, sigma = 1):
        Distribution.__init__(self, mu, sigma)


    def calculate_mean(self):
        self.mean = 1.0 * sum(self.data)/ len(self.data)
        return self.mean

        """Method to calculate the mean of the data set.

        Args:
            None

        Returns:
            float: mean of the data set

        """

        pass



    def calculate_stdev(self, sample=True):


        """Method to calculate the standard deviation of the data set.

        Args:
            sample (bool): whether the data represents a sample or population

        Returns:
            float: standard deviation of the data set

        """
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)
        mean = self.mean

        sigma  = 0
        for d in self.data:
            sigma += (d-mean) ** 2
        sigma = math.sqrt(sigma/n)
        self.stdev= sigma
        return self.stdev


        pass

    def __add__(self,other):

        """This method adds the mean of the both gaussian
        distributions and also the adds both standard deviations"""


      result = Gaussian()
      result.mean = self.mean + other.mean
      result.stdev = math.sqrt(self.stdev ** 2 + other.stdev ** 2)

      return result



    def __repr__(self):
        """This method returns the result of the mean and
        the standard deviation"""

       return "mean {}, standard deviation {}".format(self.mean, self.stdev)
