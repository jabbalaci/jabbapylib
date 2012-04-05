#!/usr/bin/python

"""
A simple API for http://developer.wordnik.com/docs /word.

To use this API, you'll need an API key, which you can get 
at http://api.wordnik.com/signup .

Once you got your API key, put it in the following file: ~/wordnik.txt

# from jabbapylib.dictionary import wordnik
"""

import json
from jabbapylib.web.web import get_page
from jabbapylib.filesystem import fs
from jabbapylib.platform import platform
from urllib import quote

WORDNIK = '{home}/wordnik.txt'.format(home=platform.get_home_dir())

############
## common ##
############

def add_api_key(url):
    """
    Adds your API key to the end of the URL.
    """
    key = fs.read_first_line(WORDNIK)
    sep = '&' if '?' in url else '?'
    return '{url}{sep}api_key={key}'.format(url=url, sep=sep, key=key)

def prepare_url(template, word):
    """
    Put the URL to be called together.
    """
    word = quote(word)
    url = template.format(word=word)
    url = add_api_key(url)
    return url

def encode(s):
    """
    For printing unicode characters to the console.
    """
    return s.encode('utf-8')

##############
## examples ##
##############

def examples(word, limit=None):
    """
    Fetch examples.
    """
    template = 'http://api.wordnik.com//v4/word.json/{word}/examples'
    url = prepare_url(template, word)
    #print url
    try:
        decoded = json.loads(get_page(url))
        #print json.dumps(decoded)
        li = []
        array = decoded['examples']     # no limit, everything
        if limit:                       # if limit specified
            array = array[:limit] 
        for e in array:
            li.append(e['text'])
        #
        return li
    except:
        return None

def print_examples(word, limit=None):
    """
    Print examples in a nice way.
    """
    li = examples(word, limit)
    if li:
        print '===Examples==='
        for index, ex in enumerate(li):
            cnt = index + 1
            print '({cnt}) {ex}'.format(cnt=cnt, ex=encode(ex))

###################
## definition(s) ##
###################

def definitions(word):
    """
    Fetch the definition of the word.
    """
    template = 'http://api.wordnik.com//v4/word.json/{word}/definitions?includeRelated=false&includeTags=false&useCanonical=false'
    url = prepare_url(template, word)
    try:
        decoded = json.loads(get_page(url))
        #print json.dumps(decoded)
        #
        partOfSpeech = decoded[0]['partOfSpeech']
        text = decoded[0]['text']
        d = {}
        d['partOfSpeech'] = partOfSpeech
        d['text'] = text
        return d
    except:
        return None

def print_definition(word):
    """
    Print the definition in a nice way.
    """
    d = definitions(word)
    if d:
        print """===Definition===
({pos})
{text}""".format(pos=encode(d['partOfSpeech']), text=encode(d['text']))

#############################################################################

if __name__ == "__main__":
    word = 'barkeeper'
    print_definition(word)
    print_examples(word, limit=None)
    