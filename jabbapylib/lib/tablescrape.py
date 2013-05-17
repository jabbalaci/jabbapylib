#!/usr/bin/env python
# Parse html tables from a given URL and output CSV.
#
# From http://stackoverflow.com/questions/2611418/scrape-html-tables-from-a-given-url-into-csv
#
# Note: To install a missing python module foo do "easy_install foo"
#   (or the new way is "pip install foo" but you might have to do 
#    "easy_install pip" first)

from BeautifulSoup import BeautifulSoup
import urllib2
import re
import sys
import unicodedata
#from time import sleep

# from http://stackoverflow.com/questions/1197981/convert-html-entities
def asciify2(s):
  matches = re.findall("&#\d+;", s)
  if len(matches) > 0:
    hits = set(matches)
    for hit in hits:
      name = hit[2:-1]
      try:
        entnum = int(name)
        s = s.replace(hit, unichr(entnum))
      except ValueError:
        pass

  matches = re.findall("&\w+;", s)
  hits = set(matches)
  amp = "&amp;"
  if amp in hits:
    hits.remove(amp)
  for hit in hits:
    name = hit[1:-1]
    if htmlentitydefs.name2codepoint.has_key(name):
      #s = s.replace(hit, unichr(htmlentitydefs.name2codepoint[name]))
      s = s.replace(hit, "")
  s = s.replace(amp, "&")
  return s

def opensoup(url):
  request = urllib2.Request(url)
  request.add_header("User-Agent", "Mozilla/5.0")
  # To mimic a real browser's user-agent string more exactly, if necessary:
  #   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.14) 
  #   Gecko/20080418 Ubuntu/7.10 (gutsy) Firefox/2.0.0.14
  pagefile = urllib2.urlopen(request)
  soup = BeautifulSoup(pagefile)
  pagefile.close()
  return soup

def asciify(s):
  #print "DEBUG[", type(s), "]"
  return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')

# remove extra whitespace, including stripping leading and trailing whitespace.
def condense(s):
  s = re.sub(r"\s+", " ", s, re.DOTALL);  #$s =~ s/\s+/\ /gs;
  return s.strip()

# this gets rid of tags and condenses whitespace
def striptags(s):
  #print "DEBUG[", type(s), "]"
  s = re.sub(r"\<span\s+style\s*\=\s*\"display\:none[^\"]*\"[^\>]*\>[^\<]*\<\/span\>",
             "", s)
  s = re.sub(r"\&\#160\;", " ", s)
  return condense(re.sub(r"\<[^\>]*\>", " ", s))

if(len(sys.argv) == 1):  # called with no arguments
  print "Usage: ", sys.argv[0], " url [n]"
  print "  (where n indicates which html table to parse)"
  exit(1)
if(len(sys.argv) == 2):  # called with just a URL
  url = sys.argv[1]
  soup = opensoup(url)
  tables = soup.findAll("table")
  print "Number of html tables: ", len(tables)
  i = 0;
  for t in tables:
    i += 1
    print str(i)+": ",
    j = 0
    hdr = t.find('tr')
    hdrl = []
    #print "DEBUGH: ", hdr.__class__, " [", hdr, "]"
    for h in hdr.findAll(re.compile('td|th')):
      j += 1
      hdrl.append(asciify2(striptags(h.renderContents()))[0:20])
    sys.stdout.write("[%3d cols, %3d rows] " % (j, len(t.findAll('tr'))))
    print " | ".join(hdrl)
  exit(0)

url = sys.argv[1]
n = int(sys.argv[2])

soup = opensoup(url)
tables = soup.findAll("table")  #, {"class":"wikitable sortable"})
table = tables[n-1]

for r in table.findAll('tr'):
  rl = []
  for c in r.findAll(re.compile('td|th')):
    rl.append(striptags(c.renderContents()))
  print " | ".join(rl)

