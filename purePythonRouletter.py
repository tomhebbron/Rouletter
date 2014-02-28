"""

This file, Rouletter.py, contains python implementations (with the same interface)
as the Cython implementation. Only advised for performance comparison purposes.

"""

import random
import bisect
import numpy

class RouletteSelector:
    '''Simulates a roulette wheel with user-defined slot sizes.'''
    bounds = []

    def __init__(self, data):
        ''' Set up the slot boundaries according to the relative sizes of data given.'''
        self.slots = len(data)
        self.bounds = [0] * self.slots
        total = sum(data)
        self.bounds = numpy.cumsum(data/float(total)) # must cast total, or you get all zero.
        
        ##Original implementation removed in favour of the numpy.cumsum version.
        #bound = 0.0
        #for i in xrange(0, self.slots):
        #    fitness = float(data[i]) / float(total)
        #    bound += fitness
        #    self.bounds[i] = bound
        ##assert(numpy.allclose(self.bounds,numpy.cumsum(data/float(total)))))

    def spin0(self, luck):
        for i in xrange(0, self.slots):
            if self.bounds[i] > luck:
                return i
        return self.slots

    def spin(self, luck):
        '''luck is a float between 0.0 and 1.0'''
        return bisect.bisect_left(self.bounds, luck)


class RouletteSelector2:
    '''Simulates a roulette wheel with user-defined slot sizes.'''

    """
    This implementation is slightly different - taken from Stack Overflow answer by user97370
    http://stackoverflow.com/a/8463663/717989
    on page http://stackoverflow.com/questions/177271/roulette-selection-in-genetic-algorithms
    
    Updated to use numpy.cumsum for speed.
    """
    
    bounds = []

    def __init__(self, data):
        #self.bounds = [sum(data[:i + 1]) for i in xrange(len(data))]
        self.bounds = numpy.cumsum(data)

    def spin(self, luck):
        '''luck is a float between 0.0 and 1.0'''
        return bisect.bisect_left(self.bounds, self.bounds[-1] * luck)

