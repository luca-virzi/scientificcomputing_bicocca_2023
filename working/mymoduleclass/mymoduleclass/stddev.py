"""function that computes the standard deviation of an array"""

import numpy as np


def stddev(a):
    ''' Given an array, it computes the standard deviation of the sample. '''
    
    mean = a.sum()/len(a)
    squares = (a-mean)**2
    sum_res = squares.sum()
    sigma = np.sqrt(sum_res/len(a))
    return sigma