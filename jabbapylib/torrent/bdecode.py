#!/usr/bin/env python

"""
based on http://effbot.org/zone/bencode.htm
"""

import re
import sys
import pprint
import copy
from cStringIO import StringIO
from jabbapylib.number.number import sizeof_fmt

pp = pprint.PrettyPrinter(indent=4)


class BDecoder:
    
    def __init__(self, fname):
        self.fname = fname
        self.data = open(fname, 'rb').read()
        self.long_torrent = self._decode(self.data)
        
        self.short_torrent = copy.deepcopy(self.long_torrent)
        del self.short_torrent['info']['pieces']        # pieces are too long, remove them
        
        self.name = self.short_torrent['info']['name']  # name of the torrent
        self.length = self._get_length()                # total length of files in bytes
        self.pretty_length = sizeof_fmt(self.length)    # total length of files in pretty format
        
    def get_info(self):
        buf = StringIO()
        old_stdout = sys.stdout
        sys.stdout = buf
        pp.pprint(self.short_torrent)   # here
        result = buf.getvalue()
        buf.close()
        sys.stdout = old_stdout
        #
        return result
    
    #########################################################################
        
    def _get_length(self):
        try:
            # consists of several files
            length = 0
            for f in self.short_torrent['info']['files']:
                length += f['length']
            #
            return length
        except KeyError:
            # consists of one file
            return self.short_torrent['info']['length']

    def _tokenize(self, text, match=re.compile("([idel])|(\d+):|(-?\d+)").match):
        i = 0
        while i < len(text):
            m = match(text, i)
            s = m.group(m.lastindex)
            i = m.end()
            if m.lastindex == 2:
                yield "s"
                yield text[i:i+int(s)]
                i = i + int(s)
            else:
                yield s
    
    def _decode_item(self, next, token): #@ReservedAssignment
        if token == "i":
            # integer: "i" value "e"
            data = int(next())
            if next() != "e":
                raise ValueError
        elif token == "s":
            # string: "s" value (virtual tokens)
            data = next()
        elif token == "l" or token == "d":
            # container: "l" (or "d") values "e"
            data = []
            tok = next()
            while tok != "e":
                data.append(self._decode_item(next, tok))
                tok = next()
            if token == "d":
                data = dict(zip(data[0::2], data[1::2]))
        else:
            raise ValueError
        return data
    
    def _decode(self, text):
        try:
            src = self._tokenize(text)
            data = self._decode_item(src.next, src.next())
            for token in src: # look for more tokens @UnusedVariable
                raise SyntaxError("trailing junk")
        except (AttributeError, ValueError, StopIteration):
            raise SyntaxError("syntax error")
        return data

#############################################################################

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "{prg}: error: specify a .torrent file".format(prg=sys.argv[0])
        sys.exit(1)
    # else
    torrent = BDecoder(sys.argv[1])
    print torrent.get_info()
    print torrent.name
    #print torrent.length
    print torrent.pretty_length
    
#    for file in torrent["info"]["files"]:
#        print "%r - %d bytes" % ("/".join(file["path"]), file["length"])
