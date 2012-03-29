import os
import re
from jabbapylib.dictionary import wordnik


def test_wordnik_txt():
    assert os.path.isfile(wordnik.WORDNIK)
    
def test_add_api_key():
    url = 'http://host/file'
    assert re.search('^http://host/file\?api_key=[0-9a-f]+$', wordnik.add_api_key(url))
    #
    url = 'http://host/file?something'
    assert re.search('^http://host/file\?something&api_key=[0-9a-f]+$', wordnik.add_api_key(url))
    
def test_examples():
    word = 'barkeeper'
    #
    examples = wordnik.examples(word)
    assert len(examples) > 0
    for e in examples:
        assert word in e
    #
    example = wordnik.examples('barkeeper', limit=1)
    assert len(example) == 1
    assert word in example[0]
    
def test_definitions():
    word = 'barkeeper'
    d = wordnik.definitions(word)
    assert d['partOfSpeech'] == 'noun'
    assert 'bar' in d['text']
