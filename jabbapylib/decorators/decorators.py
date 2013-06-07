#!/usr/bin/python

"""
Some useful decorators.

dec_time:
    print debug info when entering a function
    print debug info when quitting a function
    print elapsed time while executing the function

dec_requires:
    Useful if you call external programs/commands.
    If the given command doesn't exist, you will get
    an error immediately.

# from jabbapylib.decorators.decorators import dec_time
# from jabbapylib.decorators.decorators import dec_requires
"""

import time
from jabbapylib.filesystem import fs
import sys
import os


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


def dec_requires(fpath):
    def _decorator(fn):
        if not fs.which(fpath):
            print "Error: {f} doesn't exist".format(f=fpath)
            print "Traceback: {func}() in {src}".format(func=fn.__name__, src=__file__)
            sys.exit(1)
        #
        def step_func(*args, **kwargs):
            return fn(*args, **kwargs)
        return step_func
    return _decorator


@dec_time
def wait():
    time.sleep(3)


@dec_requires("date")
# @dec_requires("vim")    ## you could register several requirements
def something():
    os.system("date")

#############################################################################

if __name__ == "__main__":
    wait()
    something()
