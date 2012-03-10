# import scr_examples as ex

HTML_1 = """
<html>
    <table>
        <tr><td>Header</td></tr>
        <tr><td>Want This</td></tr>
    </table>
    <a href="http://google.ca">Google.ca</a>
</html>
"""

UGLY = """
<html>
<h1>Hello, World!
"""

FRAGMENT = """
<table>
    <tr><td>Header
    <tr><td>Want This
</table>
"""


LINKS = """
<html>
<head>
<title>retrogames.com</title>
</head>
<a href="http://retrogames.com">Retro Games HQ</a>
<a href="/games/elite">Elite</a>
<a href="/games/commando">Commando</a>
</html>
"""


TEXT = """
Elite can be found at http://retrogames.com/games/elite .
Commando is located at http://retrogames.com/games/commando .
"""


TIDY_IN = """<html>
 <body>
  <ul>
   <li>
    abc
   </li>
   <li>
    def
   </li>
   <li>
    ghi
   </li>
  </ul>
 </body>
</html>"""


TIDY_OUT = """<html>
<head>
  <title></title>
</head>

<body>
  <ul>
    <li>abc</li>

    <li>def</li>

    <li>ghi</li>
  </ul>
</body>
</html>
"""