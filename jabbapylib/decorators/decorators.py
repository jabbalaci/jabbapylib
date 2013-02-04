#!/usr/bin/python

"""
Some useful decorators.

dec_time:
    print debug info when entering a function
    print debug info when quiting a function
    print elapsed time while executing the function

# from jabbapylib.decorators.decorators import dec_time
"""

import time


def dec_time(func):
    def wrapper(*arg):
        start = time.time()
        print '# dec_time: enter', func.func_name
        try:
            return func(*arg)
        finally:
            print '# dec_time: exit {} ({} sec.)'.format(func.func_name, time.time() - start)
    #
    return wrapper


@dec_time
def wait():
    time.sleep(3)

#############################################################################

if __name__ == "__main__":
    wait()