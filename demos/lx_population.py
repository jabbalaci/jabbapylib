#!/usr/bin/env python

"""
Demo for lx.py.
Download population of countries.
"""

import re

from jabbapylib.web.scraper import lx
from jabbapylib.web.web import get_page


def process(doc):
    data = {}
    
    for row in doc.cssselect('tr'):
        cols = row.cssselect('td')
        if cols:
            rank = cols[0].text
            if rank and re.search('^\d+$', rank):
                country = cols[1].cssselect('a[title]')[0].text
                population = int(cols[2].text.replace(',', ''))  
                data[country] = population
                
    print data

#############################################################################

if __name__ == "__main__":
    url = 'https://secure.wikimedia.org/wikipedia/en/wiki/List_of_countries_by_population'
    text = get_page(url)
    doc = lx.to_doc(text)
    process(doc)