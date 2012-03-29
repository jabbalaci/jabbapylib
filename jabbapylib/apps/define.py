#!/usr/bin/python

"""
An interactive mini dictionary.

In Google, you can use the search term "define:word" to
get the definition of a given word. Google can also 
pronounce the word.

This script gives similar functionalities from the command-line.
Usage: just type in a word.
"""

import os
import sys
import cmd
from jabbapylib.say.say import say_with_google as say
from jabbapylib.dictionary import wordnik

__version__ = '0.1.0'


def clear():
    os.system('clear')
    #
    width = 42
    print '-' * width
    print """Jabba's Interactive Mini Dictionary v{ver}
q - quit | c - clear""".format(ver=__version__)
    print '-' * width  
    
def process(word):
    say(word, autoremove=False, background=True)
    wordnik.print_definition(word)
    wordnik.print_examples(word, limit=2)
    
class LoopCmd(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.setPrompt()
  
    def setPrompt(self):
        self.prompt = '>>> '
  
    def emptyline(self):
        pass
        
    def do_EOF(self, line):
        print
        sys.exit(0)
        
    def do_q(self, line):
        sys.exit(0)
        
    def do_c(self, line):
        clear()
        
    def default(self, line):
        process(line)
      
#############################################################################

if __name__ == "__main__":
    d = LoopCmd()
    d.do_c(None)
    try:
        d.cmdloop()
    except KeyboardInterrupt:
        print
        sys.exit(0)
