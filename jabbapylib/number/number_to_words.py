#!/usr/bin/env python

"""
Take a number and convert it to words. Examples:

1 to 5 are written out in words as: one, two, three, four, five.
115: one hundred and fifteen
342: three hundred and forty-two

The use of "and" when writing out numbers is in compliance with British usage.

Currently you can pick a number from 1 to 1000 (included).

# from jabbapylib.number import number_to_words as ntw
"""

import sys

numbers = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
   '100': 'one hundred',
  '1000': 'one thousand',
}


def length_1(s):
    return numbers[s]

def length_2(s):
    if s[0] == '1' or s[1] == '0':
        return numbers[s]
    else:
        if int(s[0]) > 1:
            tmp = s[0] + '0'
            return "{0}-{1}".format(numbers[tmp], numbers[s[1]])
    

def length_3(s):
    head = s[0]
    tail = s[1:]
    if tail == "00":
        return "{0} hundred".format(length_1(head))
    else:
        if tail[0] == "0":
            tail = tail[1]
            return "{0} hundred and {1}".format(length_1(head), length_1(tail))
        else:
            return "{0} hundred and {1}".format(length_1(head), length_2(tail))


def length_4(s):
    return numbers[s]


def convert(n):
    assert 1 <= n <= 1000
    #
    s = str(n)
    if len(s) == 1:
        return length_1(s)
    elif len(s) == 2:
        return length_2(s)
    elif len(s) == 3:
        return length_3(s)
    elif len(s) == 4:
        return length_4(s)

#############################################################################

if __name__=="__main__":
    if len(sys.argv) == 1:
        print "Error: provide a number between 1 and 1000 (included)."
        sys.exit(1)
    # else
    print '{n}: {words}'.format(n=sys.argv[1], words=convert(int(sys.argv[1])))
