#!/usr/bin/env python

"""
Upload an image to imgur anonymously.

# from jabbapylib.imgur import imgur
"""

from jabbapylib import config as cfg
import pycurl
import cStringIO
import untangle


def upload_from_computer(fpath):
    """
    Upload an image from the local machine.
    The return value is an XML string.
    
    Beware! fpath must be normal string, not unicode!
    With unicode it'll drop an error.
    """
    response = cStringIO.StringIO()
    c = pycurl.Curl()

    values = [("key", cfg.IMGUR_KEY),
              ("image", (c.FORM_FILE, fpath))]

    c.setopt(c.URL, "http://api.imgur.com/2/upload.xml")
    c.setopt(c.HTTPPOST, values)
    c.setopt(c.WRITEFUNCTION, response.write)
    c.perform()
    c.close()

    return response.getvalue()


def upload_from_web(url):
    """
    Upload an image from the web.
    The return value is an XML string.
    """
    response = cStringIO.StringIO()
    c = pycurl.Curl()

    values = [("key", cfg.IMGUR_KEY),
              ("image", url)]

    c.setopt(c.URL, "http://api.imgur.com/2/upload.xml")
    c.setopt(c.HTTPPOST, values)
    c.setopt(c.WRITEFUNCTION, response.write)
    c.perform()
    c.close()

    return response.getvalue()


def process(xml):
    """
    Process the returned XML string.
    """
    o = untangle.parse(xml)
    url = o.upload.links.original.cdata
    delete_page = o.upload.links.delete_page.cdata

    print '# url:        ', url
    print '# delete page:', delete_page
    
##########################
## some simple wrappers ##
##########################

def upload_local_img(fpath):
    """
    Upload a local image.
    The return value is a tuple: (imgur_url, imgur_delete_url)
    """
    xml = upload_from_computer(fpath)
    o = untangle.parse(xml)
    url = o.upload.links.original.cdata
    delete_page = o.upload.links.delete_page.cdata
    return (url, delete_page)

def upload_web_img(url):
    """
    Upload a web image.
    The return value is a tuple: (imgur_url, imgur_delete_url)
    """
    xml = upload_from_web(url)
    o = untangle.parse(xml)
    url = o.upload.links.original.cdata
    delete_page = o.upload.links.delete_page.cdata
    return (url, delete_page)

#############################################################################

if __name__ == "__main__":
#    img = '/tmp/test.jpg'
#    xml = upload_from_computer(img)
#    process(xml)
    #
#    url = '...'
#    xml = upload_from_web(url)
#    print xml
#    process(xml)
    #
#    print upload_local_img('/tmp/test.jpg')
    #
#    print upload_web_img(url)
    pass
