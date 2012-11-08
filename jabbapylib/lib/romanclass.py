#!/usr/bin/env python

"""
A class defining a subset of integers as Roman Numerals

defining their input and output in Roman notation 
(rather than arabic decimal notation as is usual for integers)
the internal value is in binary. 
"""

# Roman Number Converter & Class 
#   original version by James T. Dennis (c)2001 <jimd at starshine.org>
#
# refactored MMIX-II-III by Vernon Cole
#  (added class definition and made into a module.
#  (added support for unicode, extending the range to 0 <= n < 600000.
#  (added ZERO, which may be encoded as 0, '', 'N', 'nvlla' or 'NULLA' -- will print out as 'Nulla'
#  (will accept 'J' as a last digit which is = 'I'
#
# update 2009-11-23 borrowing code from roman.py by Mark Pilgrim
#    copyright 2001 (Mark Pilgrim) using Python License
#  (added RomanError exceptions
#  This module is (almost) a superset Mark's, with a very similar API --
#    the fromRoman() and toRoman() methods use the same arguments.
#  For most users expecting Mark's module, this will operate as expected.
#
# This module should feel much like the built in decimal module.
#  
# Idiosycrasy warning:  the order of arguments to binary math functions
#  IS significant -- the result will be the type of the LEFT argument.
#>>> two = roman.Roman(2)
#>>> two + 2
#Roman(4)
#>>> 2 + two
#4
#  (note: the Roman(100000), 50000, 10000 and Roman(5000) characters are unicode
#  (code points, so you must have a correct font such as "Code2000"
#  (to display values > 3999. Some consoles, such as Windows cmd, cannot
#  (print them. 
#
#  (refactored fromRoman function -
#  (will silently accept almost any jumble of IVXLCDM
#  (or will accept any unicode code point which is a numeric letter
#  (  -- i.e. where unicodedata.numeric() is defined
#  (No attempt is made to demand modern normalization of input strings.
#  (see http://en.wikipedia.org/wiki/Roman_numerals

#  This code is released and licensed under the terms of the GPL
#  or, at the user's option, the BSD license as specified at the
#  following URLs:
#   http://www.freebsd.org/copyright/freebsd-license.html
#   http://www.gnu.org/copyleft/gpl.html
#
#   In any event it is provided free of charge, "as-is" and wholly
#   without any warranty.   Use it, mangle it, incorporate it into
#   any software that will have it.

from __future__ import print_function #works on python 2.6 and up

__author__ = "Vernon Cole <vernondcole at gmail.com> with thanks to James T. Dennis"
__version__ = "1.0.1"

try:
    import unicodedata
    unicodeWorks = True
except:
    unicodeWorks = False  # IronPython workaround
#Define exceptions
class RomanError(ValueError): pass
class OutOfRangeError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass

class Roman(int):     #define "Roman" as a subset of int
    """Class Roman is a subset of "int"
    define by: Roman(123) or Roman('123') or Roman('CXXIII')"""    
    def __new__(cls,N=0):
        if isinstance(N,(str,unicode)): #if arg is a string
            try:
                n = int(N)              # may be a decimal string
            except ValueError:
                try:
                    n = fromRoman(N)    # or may be a roman number
                except InvalidRomanNumeralError:
                        raise InvalidRomanNumeralError, \
                            'Not a valid Roman or Arabic number:"%s"'%N
        else:
            n = int(N)                     # or a numeric value
        if n < 0 or n > 599999:
            raise OutOfRangeError, 'Cannot store "%s" as Roman' % repr(N)
        return int.__new__(cls,n)           # store as an int

    def __str__(self):
        return toRoman(self.__int__())      # print out as Roman number

    def __repr__(self):
        return 'Roman(%d)' % self.__int__() # reveal what's inside

    def __len__(self):
        return len(toRoman(self.__int__()))
    def __add__(self,other):                # so that II + II = IV
        return Roman(self.__int__() + other)
    def __sub__(self,other):
        return Roman(self.__int__() - other)
    def __mul__(self,other):
        return Roman(self.__int__() * other)
    def __floordiv__(self,other):
        return Roman(self.__int__() // other)
    def __getattr__(self,name):   # in case someone tries roman.value
        if name == 'value':
            return self.__int__()
        raise AttributeError, 'Type Roman does not define "%s"'%name
    
# Convert natural numbers to their Roman numeral representations 
# and vice versa.

# First we associate a dictionary of numeric values with
# their Roman numeral (string token) equivalents as follows:
_Rom={ #unicode code points for large Roman Numerals
 u"\u2188":100000, #looks like a letter I overprinted with three coincentric circles -- http://commons.wikimedia.org/wiki/File:U%2B2188.svg
 u"\u2182\u2188":90000,
 u"\u2187":50000,  #looks like half of u2188 or 3 D's -- http://commons.wikimedia.org/wiki/File:U%2B2187.svg
 u"\u2182\u2187":40000,
 u"\u2182":10000,  #looks like two coincentric circles on a vertical bar -- http://www.fileformat.info/info/unicode/char/2182/index.htm
 u"M\u2182":9000,
 u"\u2181":5000, #looks like two overprinted D's -- http://www.fileformat.info/info/unicode/char/2181/index.htm
 u"M\u2181":4000,
 u"M":1000,   # regular ASCII letters for regular size Roman Numerals
 u"CM":900,
 u"D": 500,
 u"CD":400, 
 u"C": 100,
 u"XC": 90,
 u"L":  50,
 u"XL": 40,
 u"X":  10,
 u"IX":  9,
 u"V":   5,
 u"IV":  4,
 u"I":   1,
 u"J":1 #used as the final 'I' in some ancient texts
 }
# We also create a sequence tuple in descending order.
# It's for interating over the value list in a convenient order.

# We include the two-letter tokens (IV, CM, CD, XC, etc) because
# it makes our main conversion loop simpler (as we'll see).
# Basically it means we can loop straight through without having
# to encode a bunch of parsing conditionals (the sequence, including
# the two letter tokens already incorporates most the the parsing
# rules for roman numeral strings).  

_RomSeq = ( u"\u2188",u"\u2182\u2188",u"\u2187",u"\u2182\u2187",u"\u2182",u"M\u2182", u"\u2181", u"M\u2181",
           u"M", u"CM", u"D", u"CD", u"C", u"XC", u"L", u"XL", 
       u"X", u"IX", u"V", u"IV", u"I", u"J" )
# This allows us to convert from binary to Roman in about 7 lines 
# of code; and from Roman back to binary less than 20

def toRoman(N):
    "format a binary number as a Roman unicode string."
    if N == 0: return u'Nulla' # printable value for Zero is "Nulla"
    # or "Nvlla" but I think the 'u' easier to read than the Latin 'v'
    n = int(N)
    if n < 0 or n > 599999:
        raise OutOfRangeError, 'Cannot convert "%s" to Roman' % repr(N)
    result=""
#   Our result starts as an empty string.
# We interate over the sequence of roman numeral component strings
# if the corresponding value (the value associated with "M" or "CM", etc)
# is greater than our number, we append the current string to 
# our result and subtract its corresponding value from our copy of n
    for s in _RomSeq:  # try each component string
        while n >= _Rom[s]: # until it is no longer in range
            result = result + s # string concatenation (not addition)
            n -= _Rom[s]        # mathmatical subtraction
    return result

def fromRoman(S):
    "Convert a roman numeral string to binary"
    if type(S) is Roman: return int(S) #in case it already IS Roman
    result=0
    # Start by converting to upper case for convenience
    us = S.strip().upper()
    try:
        s = unicode(us)
    except UnicodeEncodeError: # IronPython bug
        s = us
    #test for zero
    if s == '' or s == u'N' or s[:5] == u'NULLA':  # Latin for "nothing"
        return 0
# This simplified algorithm (V.Cole) will correctly convert any correctly formed
# Roman number. It will also convert lots of incorrectly formed numbers, and will
# accept any combination of ASCII 'MCDLXVI' and unicode Roman Numeral code points.
    held = 0    # this is the memory for the previous Roman digit value
    for c in s:    #this will get the value of a sequence of unicode Roman Numeral points
        try:        # may be a normal alphabetic character
            val = _Rom[c]  #pick the value out of the dict
        except KeyError: # may be a unicode character with a value
            try: 
                val = int(unicodedata.numeric(c))  # retrieve the value from the unicode chart
            except:
                raise InvalidRomanNumeralError, 'incorrectly formatted Roman Numeral '+repr(S) 

        if val > held:    # if there was a smaller value to the left, subtract it
            result -= held
        else:             # otherwise add it
            result += held 
        held = val        # try this loop's letter value on the next loop
    result += held  #the last letter value is always added
    return result

def toUnicodeRoman(N):
    """format a binary number into a true unicode Roman string.
    so you get \u2160 rather than "I" etc."""
    n = int(N)
    ##if n == 0: return u'\u0bbf' # ideographic number Zero
    if 0 < n <= 12:
        return unichr(0x215f + n) # I to XII as a single code point
    s = toRoman(N)
    # put in the true unicode points rather than the ASCII look alikes
    s = s.replace(u'I',u'\u2160').replace(u'V',u'\u2164').replace(u'X',u'\u2169')
    s = s.replace(u'L',u'\u216c').replace(u'C',u'\u216d').replace(u'D',u'\u216e').replace(u'M',u'\u216f')
    return s
#----------------------------------------- Test program follows ---------------------------------
# The following simply prints a list by converting to a roman number *and back*.
def test():
    longest=""
    mini = Roman()
    bigList = []
    i = Roman(0)
    while i < 4007:
        rs = Roman(i)
        j = fromRoman(rs)
        assert i == j, '%d -> %s -> %s' % (i,repr(rs),j) 
        
        if len(rs) > len(longest): #Roman has a len() method
            longest = rs
        mini = min(mini,i) #integer functions should work
        bigList.append(rs)
        i += 1
    maxi = max(bigList)
    print('The longest number between %s and '% mini,end=' ')
    try:
            print(maxi)
    except UnicodeEncodeError:
            print(repr(maxi))
    print ('was "%s" which is "%d" in Arabic' % (longest, longest))
    assert fromRoman(longest) == 3888
    
    ## -- now test some sample convertions ---------------------------------------------
    assert fromRoman('IIIJ') == 4  # test that the archaic construction works
    try:
        s = toRoman(-1)
        assert False, "toRoman(-1) should fail"
    except OutOfRangeError:
        pass
    try:
        s = Roman(1000000)
        assert False, "roman.Roman(10000000) should fail"
    except OutOfRangeError:
        pass
    try:
        i = fromRoman('XXY')
        assert False, "fromRoman('XXY') should fail"
    except InvalidRomanNumeralError:
        pass
    assert toRoman(0) == u'Nulla' # zero really needs to be printable
    assert toRoman('3') == u'III' # Arabic string literals work
    assert toRoman(12.1) == u'XII' # float numbers are tuncated
    assert Roman('DCLXVI') == 666  # class instances work as integers
    r = Roman('MDCCCCX')  # malformed input - as 1910 on Admiralty Arch in London.
    if str(r) != r.__str__():
        print('Error in type object use of str(). [IronPython?]')
    assert r.__str__()  == 'MCMX' # output is normalized Roman form
    two = Roman(2)
    four = two + two # addition works
    assert four.__str__() == 'IV' # result prints as a Roman numeral
    eight = two * four # multiplication works
    assert eight.__str__() == 'VIII'
    sixteen = Roman('XVI')
    assert sixteen.value == 16  # if a programmer tries, we can get the .value
    assert sixteen // Roman('V') == Roman('III') # floor division works
    assert (sixteen - four).__str__() == 'XII' # subtraction works
    if unicodeWorks:
        assert Roman(u'\u217b') == 12 #unicode Roman number 'xii' as a single charactor
        assert Roman(u'\u2167') == 8   #unicode Roman number 'VIII'
        assert Roman(u'\u2160\u216f') == 999  #unicode 'IM' which is a badly formed number
        assert fromRoman(u'\u2182\u2182\u2182\u2182\u2181MMMCCLXIJ') ==  48262
        assert fromRoman(u'\u2188\u2182\u2187\u2181v') == 145005

    assert toUnicodeRoman(166447) == \
    u'\u2188\u2187\u2182\u2181\u216f\u216d\u216e\u2169\u216c\u2164\u2160\u2160'
    assert toUnicodeRoman(12) ==  u'\u216b'
    
    nl = [5000,10000,50000,100000]
    for nb in nl:
        n = toRoman(nb)
        try: 
            nn = unicodedata.numeric(n)
            name = unicodedata.name(n)
        except ValueError:
            nn = '<<ValueError -- Python issue 6383 still exists>>'
            name = ''
        except NameError:
            name = 'unicodedata not implemented.'
            nn = '[Iron Python?]'
        print(nb, name, nn)
        try:
            print(  'unicode=',n.encode('unicode_escape'))
        except:
            print( '  (cannot be printed here)')

if __name__ == "__main__":
    test()
