#!/usr/bin/env python

"""
Measure execution time.

This tip is from here: 
http://stackoverflow.com/questions/1685221/accurately-measure-time-python-function-takes

# from jabbapylib.dateandtime import Timer
"""

import time

class Timer(object):
    
    def __enter__(self):
        self.__start = time.time()

    def __exit__(self, type, value, traceback): #@ReservedAssignment
        # Error handling here
        self.__finish = time.time()

    def elapsed_time(self):
        return self.__finish - self.__start

    
#############################################################################
    
if __name__ == "__main__":
    timer = Timer()
    with timer:
        # Whatever you want to measure goes here
        time.sleep(1)
    
    print timer.elapsed_time()
