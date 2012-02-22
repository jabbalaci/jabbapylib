#!/usr/bin/env python

"""
Simple IMDB movie info fetcher.

Available info:

Plot Votes Rated Response Title Poster Writer ID 
Director Released Actors Year Genre Runtime Rating
"""

import json
import urllib
from jabbapylib.web.web import get_page

BASE = 'http://www.imdbapi.com/?i=&'


class Movie(object):

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = BASE + urllib.urlencode({'t' : keyword})
        self.d = self.get_info()
        
    def get_info(self):
        text = get_page(self.url)
        return json.loads(text)
    
    def __getitem__(self, key):
        return self.d[key]
    
    def __str__(self):
        li = []
        for key in self.d:
            li.append("{key}: {value}".format(key=key, value=self.d[key]))
            
        return '\n'.join(li)
    

def get_rating(title):
    m = Movie(title)
    return float(m['Rating'])

#############################################################################

if __name__ == "__main__":
    m = Movie('star wars episode 4')
    print 'Title: {title}'.format(title=m['Title'])
    print 'Year: {year}'.format(year=m['Year'])
    print 'Rating: {rating}'.format(rating=m['Rating']) 
