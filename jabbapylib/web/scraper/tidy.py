#!/usr/bin/env python

"""
Pretty print HTML. 
I didn't like the current pretty printers.

# from jabbapylib.web.scraper import tidy
"""

import jabbapylib.config as cfg
from jabbapylib.process import process

OPTIONS = '-f /dev/null --tidy-mark "no" --doctype "omit" --indent "auto" --indent-spaces "2" --wrap "90"'

def pretty_print(text):
    cmd = "{prg} {options}".format(prg=cfg.TIDY, options=OPTIONS)
    return process.get_cmd_output_input_from_stdin(cmd, text)

#############################################################################

if __name__ == "__main__":
    html = """<html>
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
    print pretty_print(html)
