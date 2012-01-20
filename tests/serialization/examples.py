# dictionary
A_DATA_1 = {
    'books' : [
        {'book' : {'name' : 'book1', 'description' : 'awesome book'}},
        {'book' : {'name' : 'book2', 'description' : 'fantastic book'}}
    ]
}

# A_DATA_1 can be converted to A_DATA_1_AS_XMLRPC and back

# XML RPC. The XML is annotated with type information => results in a fat XML.
A_DATA_1_AS_XMLRPC = """<params>
<param>
<value><struct>
<member>
<name>books</name>
<value><array><data>
<value><struct>
<member>
<name>book</name>
<value><struct>
<member>
<name>name</name>
<value><string>book1</string></value>
</member>
<member>
<name>description</name>
<value><string>awesome book</string></value>
</member>
</struct></value>
</member>
</struct></value>
<value><struct>
<member>
<name>book</name>
<value><struct>
<member>
<name>name</name>
<value><string>book2</string></value>
</member>
<member>
<name>description</name>
<value><string>fantastic book</string></value>
</member>
</struct></value>
</member>
</struct></value>
</data></array></value>
</member>
</struct></value>
</param>
</params>
"""

#####

# list
A_DATA_2 = [1978, 1979, {'key': 'value'}, 2000]

# A_DATA_2 can be converted to A_DATA_2_AS_XMLRPC and back

# fat XML RPC
A_DATA_2_AS_XMLRPC = """<params>
<param>
<value><array><data>
<value><int>1978</int></value>
<value><int>1979</int></value>
<value><struct>
<member>
<name>key</name>
<value><string>value</string></value>
</member>
</struct></value>
<value><int>2000</int></value>
</data></array></value>
</param>
</params>
"""

#############################################################################

# dictionaries and lists can be converted to JSON and back

B_DATA_1 = {
    'books' : [
        {'book' : {'name' : 'book1', 'description' : 'awesome book'}},
        {'book' : {'name' : 'book2', 'description' : 'fantastic book'}}
    ]
}

B_DATA_1_AS_JSON = '{"books": [{"book": {"name": "book1", "description": "awesome book"}}, {"book": {"name": "book2", "description": "fantastic book"}}]}'

#####

B_DATA_2 = [1978, 1979, {'key': 'value'}, 2000]

B_DATA_2_AS_JSON = '[1978, 1979, {"key": "value"}, 2000]'

#############################################################################

# normal XML (not fat XML RPC)
C_XML_1 = """<persons>
    <person>
        <name>Koen Bok</name>
        <age>26</age>
    </person>
    <person>
        <name>Plutor Heidepeen</name>
        <age>33</age>
    </person>
</persons>"""

# normal XML nicely converted to JSON
C_XML_1_AS_JSON = '{"persons": {"person": [{"age": "26", "name": "Koen Bok"}, {"age": "33", "name": "Plutor Heidepeen"}]}}'

#####

# problem here: attributes cause error for the XML2JSON converter
C_XML_2 = """<persons>
    <person sex="female">
        <name>Judy</name>
        <age>26</age>
    </person>
    <person sex="male">
        <name>Robert</name>
        <age>33</age>
    </person>
</persons>"""


##########

# JSON dictionary
D_JSON_1 = '{"persons": {"person": [{"age": "26", "name": "Koen Bok"}, {"age": "33", "name": "Plutor Heidepeen"}]}}'

# D_JSON_1 can be converted to D_JSON_1_AS_XMLRPC and back

# fat XMLRPC
D_JSON_1_AS_XMLRPC = """<params>
<param>
<value><struct>
<member>
<name>persons</name>
<value><struct>
<member>
<name>person</name>
<value><array><data>
<value><struct>
<member>
<name>age</name>
<value><string>26</string></value>
</member>
<member>
<name>name</name>
<value><string>Koen Bok</string></value>
</member>
</struct></value>
<value><struct>
<member>
<name>age</name>
<value><string>33</string></value>
</member>
<member>
<name>name</name>
<value><string>Plutor Heidepeen</string></value>
</member>
</struct></value>
</data></array></value>
</member>
</struct></value>
</member>
</struct></value>
</param>
</params>
"""

#####

# JSON list
D_JSON_2 = '[1978, 1979, {"key": "value"}, 2000]'

# D_JSON_2 can be converted to D_JSON_2_AS_XMLRPC and back

# fat XML RPC
D_JSON_2_AS_XMLRPC = """<params>
<param>
<value><array><data>
<value><int>1978</int></value>
<value><int>1979</int></value>
<value><struct>
<member>
<name>key</name>
<value><string>value</string></value>
</member>
</struct></value>
<value><int>2000</int></value>
</data></array></value>
</param>
</params>
"""
