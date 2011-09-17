#!/usr/bin/env python

"""
Demo for lx.py.
Download image URLs from wallbase.cc.
"""

from jabbapylib.web.scraper import lx
from jabbapylib.web.web import get_page


def get_jpg_image(doc):
    """Extract the URL of the JPG image from the HTML of a wallbase.cc subpage."""
    image = None

    div = doc.cssselect('div[id="bigwall"][class="right"]')[0]
    if div is not None:
        img = div.cssselect('img[src]')[0]
        if img is not None:
            image = img.get('src')

    return image


def extract_images_from_pages(pages):
    """Extract images from subpages."""
    li = []
    for page in pages:
        doc = lx.to_doc(get_page(page))
        image = get_jpg_image(doc)
        li.append(image)
        
    return [x for x in li if x]     # remove None elems


def get_subpages(doc):
    """Images can be found on separate pages. Extract the URL of these subpages."""
    pages = []
    for tag in doc.cssselect('a[class="thdraggable thlink"][target="_blank"]'):
        pages.append(tag.get('href'))
        
    return pages


def get_image_url_list(url):
    """Controller function for getting the URLs of the JPG images."""
    text = get_page(url)
    doc = lx.to_doc(text)
    
    subpages = get_subpages(doc)
    images = extract_images_from_pages(subpages)
    
    return images


#############################################################################

if __name__ == "__main__":
    url = 'http://wallbase.cc/tags/info/7964'
    for url in get_image_url_list(url):
        print url