import examples
from jabbapylib.serialization import serialize

#############################################################################
# Section A

def test_data_to_xmlrpc():
    res = serialize.data_to_xmlrpc(examples.A_DATA_1)
    assert res == examples.A_DATA_1_AS_XMLRPC
    #
    res = serialize.data_to_xmlrpc(examples.A_DATA_2)
    assert res == examples.A_DATA_2_AS_XMLRPC
    
def test_xmlrpc_to_data():
    res = serialize.xmlrpc_to_data(examples.A_DATA_1_AS_XMLRPC)
    assert res == examples.A_DATA_1
    #
    res = serialize.xmlrpc_to_data(examples.A_DATA_2_AS_XMLRPC)
    assert res == examples.A_DATA_2
    
#############################################################################
# Section B

def test_data_to_json():
    jsn = serialize.data_to_json(examples.B_DATA_1)
    assert jsn == examples.B_DATA_1_AS_JSON
    #
    jsn = serialize.data_to_json(examples.B_DATA_2)
    assert jsn == examples.B_DATA_2_AS_JSON    
    
def test_json_to_data():
    back = serialize.json_to_data(examples.B_DATA_1_AS_JSON)
    assert back == examples.B_DATA_1
    #
    back = serialize.json_to_data(examples.B_DATA_2_AS_JSON)
    assert back == examples.B_DATA_2
    
#############################################################################
# Sections C and D

def test_xml_to_json():
    res = serialize.xml_to_json(examples.C_XML_1)
    assert res == examples.C_XML_1_AS_JSON
    #
#    res = serialize.xml_to_json(examples.C_XML_2)
#    print res
    
def test_json_to_xmlrpc_1():
    xmlrpc = serialize.json_to_xmlrpc(examples.D_JSON_1)
    assert xmlrpc == examples.D_JSON_1_AS_XMLRPC
    #
    jsn = serialize.xmlrpc_to_json(xmlrpc)
    assert jsn == examples.D_JSON_1
    #
    fat_jsn = serialize.xml_to_json(xmlrpc)
    assert fat_jsn != examples.D_JSON_1
    
def test_json_to_xmlrpc_2():
    xmlrpc = serialize.json_to_xmlrpc(examples.D_JSON_2)
    assert xmlrpc == examples.D_JSON_2_AS_XMLRPC
    #
    jsn = serialize.xmlrpc_to_json(xmlrpc)
    assert jsn == examples.D_JSON_2
