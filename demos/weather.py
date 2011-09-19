#!/usr/bin/env python

"""
Weather.
"""

from jabbapylib.web.scraper import lx, scraper #@UnusedImport
from jabbapylib.web.web import get_page
from jabbapylib.dateandtime.timer import Timer #@UnusedImport


def process(url):
    text = get_page(url, user_agent=True)
    doc = lx.to_doc(text)
    #lx.show_paths(doc, find='Montreal, Quebec')
    tag = doc.cssselect('h1#locationName.brTopLeft5')[0]
    city = tag.text
    print city
    tag = doc.cssselect('div#tempActual span.pwsrt span.nobr')[0]
    celsius = tag.text_content() 
    print celsius


#############################################################################

if __name__ == "__main__":
    zip_code = 'h2x4e1'
    url = 'http://www.wunderground.com/cgi-bin/findweather/getForecast?query={zip}'.format(zip=zip_code)
    #timer = Timer()
    #with timer:
    process(url)
    #print timer.elapsed_time()