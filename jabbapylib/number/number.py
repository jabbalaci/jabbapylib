#!/usr/bin/env python

"""
Working with numbers.

# from jabbapylib.number.number import number_to_pretty_string
# from jabbapylib.number.number import sizeof_fmt

Update (20120224):
==================

There is a better way for printing numbers in a pretty way:

    import locale
     
    # Setting the locale to US English
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
     
    print "Number without formatting applied: {0}".format(65739838)
    print "Number with formatting applied: {0:n}".format(65739838)

Notice the :n in the 2nd case, which makes it use the current 
locale setting to insert the appropriate number separator characters.
"""

def number_to_pretty_string(n):
    """Converts a number to a nicely formatted string.
    
    Example: 6874 => '6,874'."""
    l = []
    for i, c in enumerate(str(n)[::-1]):
        if i % 3 == 0 and i != 0:
            l += ','
        l += c
    return "".join(l[::-1])

def sizeof_fmt(num):
    """
    Human-readable file size.
    http://stackoverflow.com/questions/1094841
    """
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
    return "%3.1f %s" % (num, 'TB')

#############################################################################
    
if __name__ == "__main__":
    number = 6874
    print number_to_pretty_string(number)   # '6,874'
    
    length = 1322688512
    print sizeof_fmt(length)
