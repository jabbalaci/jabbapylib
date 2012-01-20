from jabbapylib.serialization.xml2json import Xml2Json

xml_1 = """<doc>
  <tag>
    <subtag>data</subtag>
    <t>data1</t>
    <t>data2</t>                                                                                                                                                           
  </tag>                                                                                                                                                                   
</doc>"""

# notice the XML header
xml_2 = """<?xml version="1.0"?>
<doc>
  <tag>
    <subtag>data</subtag>
    <t>data1</t>
    <t>data2</t>                                                                                                                                                           
  </tag>                                                                                                                                                                   
</doc>"""


def test_1():
    res = Xml2Json(xml_1).result
    assert res == {u'doc': {u'tag': {u'subtag': u'data', u't': [u'data1', u'data2']}}}
    
def test_2():
    res = Xml2Json(xml_2).result
    assert res == {u'doc': {u'tag': {u'subtag': u'data', u't': [u'data1', u'data2']}}}