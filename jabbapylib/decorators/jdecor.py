#!/usr/bin/python

"""
Some useful decorators.
"jd" stands for "jabba's decorator" :)

jd_time:
    print debug info when entering a function
    print debug info when quitting a function
    print execution time of the function

jd_requires:
    Useful if you call external programs/commands.
    If the given command doesn't exist, you will get
    an error immediately.

# from jabbapylib.decorators.decorators import jd_time
# from jabbapylib.decorators.decorators import jd_requires
"""

import time
from jabbapylib.filesystem import fs
import sys
import os


def jd_time(func):
    """
    For debugging the execution time of a function.
    """
    def wrapper(*arg):
        start = time.time()
        print '# dec_time: enter', func.func_name
        try:
            return func(*arg)
        finally:
            print '# dec_time: exit {} ({} sec.)'.format(func.func_name, time.time() - start)
    #
    return wrapper


def jd_requires(fpath):
    """
    Verify if the given external command is available.

    Useful when writing "shell scripts" and you want to make
    an external call. If the command (parameter fpath) to be
    called is not available, you get an error message right away.
    """
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


@jd_time
def wait():
    time.sleep(3)


@jd_requires("date")
# @jd_requires("vim")    ## you could register several requirements
def something():
    os.system("date")

#############################################################################

if __name__ == "__main__":
    wait()
    something()
