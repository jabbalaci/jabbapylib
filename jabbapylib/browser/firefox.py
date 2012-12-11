#!/usr/bin/env python

"""
Automate your browser via telnet.
Requirements:
* Firefox
* MozRepl add-on (https://addons.mozilla.org/en-US/firefox/addon/mozrepl/)
  - activate the add-on ("Start" and "Activate on startup")

Documentation of gBrowser:
* https://developer.mozilla.org/en-US/docs/XUL/tabbrowser (reference)
* https://developer.mozilla.org/en-US/docs/Code_snippets/Tabbed_browser (code snippets)
"""

import time
import sys
import  socket
import telnetlib

HOST = 'localhost'
PORT = 4242

prompt = [r'repl\d*> ']    # list of regular expressions


def open_curr_tab(url):
    """
    Open a URL in the *current* tab.
    """
    tn = telnetlib.Telnet(HOST, PORT)
    tn.expect(prompt)
    cmd = "content.location.href = '{url}'".format(url=url)
    tn.write(cmd + "\n")
    tn.write("repl.quit()\n")


def open_new_empty_tab():
    """
    Open a new empty tab and put the focus on it.
    """
    tn = telnetlib.Telnet(HOST, PORT)
    tn.expect(prompt)
    tn.write("gBrowser.addTab()\n")
    tn.expect(prompt)
    tn.write("length = gBrowser.tabContainer.childNodes.length\n")
    tn.expect(prompt)
    tn.write("gBrowser.selectedTab = gBrowser.tabContainer.childNodes[length-1]\n")
    tn.expect(prompt)
    tn.write("repl.quit()\n")


def is_mozrepl_installed():
    """
    Test if MozRepl is installed.

    We simply try to connect to localhost:4242 where
    MozRepl should be listening.
    """
    try:
        tn = telnetlib.Telnet(HOST, PORT)
        tn.expect(prompt)
        tn.write("repl.quit()\n")
        return True
    except socket.error:
        return False


def close_curr_tab():
    """
    Close the current tab.
    """
    tn = telnetlib.Telnet(HOST, PORT)
    tn.expect(prompt)
    tn.write("gBrowser.removeCurrentTab()\n")
    tn.write("repl.quit()\n")

#############################################################################

if __name__ == "__main__":
    if not is_mozrepl_installed():
        print 'Cannot connect to localhost:4242.'
        print 'Make sure that the MozRepl Firefox add-on is installed and activated.'
        sys.exit(1)
    else:
        sec = 4
        print 'Demo'
        #
        print '* open a new tab'
        open_new_empty_tab()
        print '* wait {X} sec.'.format(X=sec)
        time.sleep(sec)
        #
        print '* open python.org in current tab'
        open_curr_tab('http://www.python.org')
        print '* wait {X} sec.'.format(X=sec)
        time.sleep(sec)
        #
        print '* close current tab'
        close_curr_tab()
        print '* done'
