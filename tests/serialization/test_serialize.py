import ser_examples as ex
from jabbapylib.serialization import serialize

#############################################################################
# Section A

def test_data_to_xmlrpc():
    res = serialize.data_to_xmlrpc(ex.A_DATA_1)
    assert res == ex.A_DATA_1_AS_XMLRPC
    #
    res = serialize.data_to_xmlrpc(ex.A_DATA_2)
    assert res == ex.A_DATA_2_AS_XMLRPC
    
def test_xmlrpc_to_data():
    res = serialize.xmlrpc_to_data(ex.A_DATA_1_AS_XMLRPC)
    assert res == ex.A_DATA_1
    #
    res = serialize.xmlrpc_to_data(ex.A_DATA_2_AS_XMLRPC)
    assert res == ex.A_DATA_2
    
#############################################################################
# Section B

def test_data_to_json():
    jsn = serialize.data_to_json(ex.B_DATA_1)
    assert jsn == ex.B_DATA_1_AS_JSON
    #
    jsn = serialize.data_to_json(ex.B_DATA_2)
    assert jsn == ex.B_DATA_2_AS_JSON    
    
def test_json_to_data():
    back = serialize.json_to_data(ex.B_DATA_1_AS_JSON)
    assert back == ex.B_DATA_1
    #
    back = serialize.json_to_data(ex.B_DATA_2_AS_JSON)
    assert back == ex.B_DATA_2
    
#############################################################################
# Sections C and D

def test_xml_to_json():
    res = serialize.xml_to_json(ex.C_XML_1)
    assert res == ex.C_XML_1_AS_JSON
    #
#    res = serialize.xml_to_json(ex.C_XML_2)
#    print res
    
def test_json_to_xmlrpc_1():
    xmlrpc = serialize.json_to_xmlrpc(ex.D_JSON_1)
    assert xmlrpc == ex.D_JSON_1_AS_XMLRPC
    #
    jsn = serialize.xmlrpc_to_json(xmlrpc)
    assert jsn == ex.D_JSON_1
    #
    fat_jsn = serialize.xml_to_json(xmlrpc)
    assert fat_jsn != ex.D_JSON_1
    
def test_json_to_xmlrpc_2():
    xmlrpc = serialize.json_to_xmlrpc(ex.D_JSON_2)
    assert xmlrpc == ex.D_JSON_2_AS_XMLRPC
    #
    jsn = serialize.xmlrpc_to_json(xmlrpc)
    assert jsn == ex.D_JSON_2
