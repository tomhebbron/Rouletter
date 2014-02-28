import unittest
import time
import random

import scipy
import numpy

import purePythonRouletter
import Rouletter

def profile_this(fn):
    ''' Decorator function for profiler - use @profile_this before definition. '''
    def profiled_fn(*args, **kwargs):
        # name for profile dump
        fpath = fn.__name__ + '.profile'
        prof = cProfile.Profile()
        ret = prof.runcall(fn, *args, **kwargs)
        prof.dump_stats(fpath)
        return ret
    return profiled_fn


def time_this(method):
    def timed_fn(*args, **kwargs):
        startTime = time.time()
        ret = method(*args, **kwargs)
        print "%r (%r, %r) %2.2f sec" % (method.__name__, args, kwargs, time.time()-startTime)
        return ret
    return timed_fn


@time_this
def repeats_test(rsType, num_wheels=1, num_spins_per_wheel=1):
    wheel_segments = numpy.random.randint(low=0,high=100,size=100)
    hits = [0] * len(wheel_segments)
    for i in xrange(num_wheels):
        rs = rsType(wheel_segments)
        for j in xrange(num_spins_per_wheel):
            hits[rs.spin(random.random())] += 1
    corr = scipy.corrcoef(wheel_segments, hits)[0,1]
    print corr
    return corr


class RouletteSelectorTests(unittest.TestCase):

    def testCorrelation(self):
        '''  Test that hits on the wheel correlate to the sizes '''
        global CURRENT_TEST_CLASS
        corr = repeats_test(CURRENT_TEST_CLASS,100,1000)
        self.failUnless(corr > 0.80 )





def main():
    global CURRENT_TEST_CLASS
    for CURRENT_TEST_CLASS in [Rouletter.RouletteSelector, purePythonRouletter.RouletteSelector, purePythonRouletter.RouletteSelector2]:
        print CURRENT_TEST_CLASS
        unittest.main(exit=False)
    
if __name__ == '__main__':
    #import cProfile
    #cProfile.run('main()','roulette.profile')
    main()
    
