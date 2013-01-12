#!/usr/bin/env python

"""
Automate your browser via telnet.
Requirements:
* Firefox
* MozRepl add-on (https://addons.mozilla.org/en-US/firefox/addon/mozrepl/)
  - activate the add-on (under Tools -> MozRepl, "Start" and "Activate on startup")

Documentation of gBrowser:
* https://developer.mozilla.org/en-US/docs/XUL/tabbrowser (reference)
* https://developer.mozilla.org/en-US/docs/Code_snippets/Tabbed_browser (code snippets)
"""

import re
import time
import sys
import  socket
import telnetlib
import json
from jabbapylib.text import ascii


class Mozrepl(object):
    """
    Based on https://github.com/bard/mozrepl/wiki/Pyrepl .
    """

    HOST = 'localhost'
    PORT = 4242
    prompt = [r'repl\d*> ']    # list of regular expressions

    def __init__(self, ip=HOST, port=PORT):
        self.ip = ip
        self.port = port

    def __enter__(self):
        self.tn = telnetlib.Telnet(self.ip, self.port)
        self.tn.expect(Mozrepl.prompt)
        return self

    def __exit__(self, type, value, traceback):
        self.tn.close()
        del self.tn

    def cmd(self, command):
        """
        Execute the command and fetch its result.
        """
        self.tn.write(command.encode() + b"\n")
        return self.tn.expect(Mozrepl.prompt)

    def get_text_result(self, command, sep=''):
        """
        Execute the command and fetch its result as text.
        """
        lines = self.cmd(command)[2].split("\n")
        if re.search(Mozrepl.prompt[0].strip(), lines[-1]):
            lines = lines[:-1]
        return sep.join(lines)

    @classmethod
    def is_installed(cls):
        """
        Test if MozRepl is installed.

        We simply try to connect to localhost:4242 where
        MozRepl should be listening.
        """
        try:
            with Mozrepl() as mr:
                pass
            return True
        except socket.error:
            return False


def open_url_in_curr_tab(url):
    """
    Open a URL in the *current* tab.
    """
    with Mozrepl() as mr:
        cmd = "content.location.href = '{url}'".format(url=url)
        mr.cmd(cmd)


def get_curr_tab_url():
    """
    URL of the current tab.
    """
    with Mozrepl() as mr:
        result = mr.cmd("content.location.href")
        return result[2].split()[0].replace('"', '')


def open_new_empty_tab():
    """
    Open a new empty tab and put the focus on it.
    """
    with Mozrepl() as mr:
        mr.cmd('gBrowser.addTab()')
        mr.cmd('length = gBrowser.tabContainer.childNodes.length')
        mr.cmd('gBrowser.selectedTab = gBrowser.tabContainer.childNodes[length-1]')


def open_url_in_new_tab(url):
    """
    Open the given URL in a new tab.

    webbrowser.open_new_tab puts the focus on Firefox.
    This one doesn't.
    """
    open_new_empty_tab()
    open_url_in_curr_tab(url)


def get_curr_tab_html():
    """
    HTML source of the current tab.
    """
    with Mozrepl() as mr:
        result = mr.cmd('content.document.body.innerHTML')
        html = result[2].split('\n')
        if html[0].strip() == '"':
            html = html[1:]
        if re.search(Mozrepl.prompt[0], html[-1]):
            html = html[:-1]
        if html[-1].strip() == '"':
            html = html[:-1]
        return ''.join(html)


def close_curr_tab():
    """
    Close the current tab.
    """
    with Mozrepl() as mr:
        mr.cmd('gBrowser.removeCurrentTab()')


def get_number_of_tabs():
    """
    Number of tabs in the browser.
    """
    with Mozrepl() as mr:
        result = mr.get_text_result('gBrowser.tabContainer.childNodes.length')
        return result


def get_curr_tab_title():
    """
    Title of the page in the current tab.
    """
    with Mozrepl() as mr:
        result = mr.get_text_result('document.title')
        return result

def get_tab_list():
    cmd = \
"""
String.prototype.format = function() {
    var formatted = this;
    for(arg in arguments) {
        formatted = formatted.replace("{" + arg + "}", arguments[arg]);
    }
    return formatted;
};

var all_tabs = gBrowser.mTabContainer.childNodes;
var tab_list = [];
for (var i = 0; i < all_tabs.length; ++i ) {
    var tab = gBrowser.getBrowserForTab(all_tabs[i]).contentDocument;
    if(tab.location != "about:blank")
        tab_list.push({"url":tab.location, "title":tab.title});
}

for (var i=0; i<tab_list.length; ++i) {
    var title = tab_list[i].title;
    title = title.replace(/"/g, "'");
    var item = '{"index": {0}, "title": "{1}", "url": "{2}"}'.format(i, title, tab_list[i].url);
    repl.print(item);
}
"""
    with Mozrepl() as mr:
        result = mr.get_text_result(cmd, sep='\n')
        li = []
        for x in result.split('\n'):
            x = ascii.strip_control_characters(x)
            li.append(json.loads(unicode(x, "ISO-8859-1")))
        #
        return li

#############################################################################

if __name__ == "__main__":
    if not Mozrepl.is_installed():
        print 'Cannot connect to localhost:4242.'
        print 'Make sure that the MozRepl Firefox add-on is installed and activated.'
        sys.exit(1)
    else:
#        sec = 4
#        print 'Demo'
#        #
#        print '* open a new tab'
#        open_new_empty_tab()
#        print '* wait {X} sec.'.format(X=sec)
#        time.sleep(sec)
#        #
#        print '* open python.org in current tab'
#        open_url_in_curr_tab('http://www.python.org')
#        print '* wait {X} sec.'.format(X=sec)
#        time.sleep(sec)
#        #
#        print '* close current tab'
#        close_curr_tab()
#        print '* done'
#
#        print get_number_of_tabs()
#        print get_curr_tab_title()
        for e in get_tab_list():
            print e