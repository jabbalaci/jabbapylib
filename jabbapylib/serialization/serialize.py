#!/usr/bin/env python

"""
Different serializations.

# from jabbapylib.serialization import serialize
"""

import json
import xmlrpclib
from xml2json import Xml2Json


def data_to_xmlrpc(data):
    # http://www.reddit.com/r/Python/comments/ole01/dictionary_to_xml_in_20_lines/
    """Return value: XML RPC string."""
    return xmlrpclib.dumps((data,))    # arg. is tuple

def xmlrpc_to_data(xml):
    # http://www.reddit.com/r/Python/comments/ole01/dictionary_to_xml_in_20_lines/
    """Return value: python data."""
    return xmlrpclib.loads(xml)[0][0]

def data_to_json(data):
    """Return value: JSON string."""
    data_string = json.dumps(data)
    return data_string

def json_to_data(data_string):
    """Return value: python data."""
    data = json.loads(data_string)
    return data

def xml_to_json(xml):
    """Return value: JSON string."""
    res = Xml2Json(xml).result
    return json.dumps(res)

def json_to_xmlrpc(data_string):
    """Return value: XML RPC string."""
    data = json.loads(data_string)
    return data_to_xmlrpc(data)

def xmlrpc_to_json(xmlrpc):
    """Return value: JSON string."""
    data = xmlrpc_to_data(xmlrpc)
    return data_to_json(data)

#############################################################################
    
if __name__ == "__main__":
    pass
