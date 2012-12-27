#!/usr/bin/env python

"""
Use Splinter in a headless way!

main() opens a window

the stuff around main() makes the window
invisible

It requires the xvfb package (sudo apt-get install xvfb).
"""

from pyvirtualdisplay import Display
from splinter.browser import Browser

url = 'http://simile.mit.edu/crowbar/test.html'


def main():
    browser = Browser()
    browser.visit(url)

    f = open("/tmp/source.html", "w")   # save the source in a file
    print >>f, browser.html
    f.close()

    browser.quit()
    print '__END__'

#############################################################################

if __name__ == "__main__":
    display = Display(visible=0, size=(800, 600))
    display.start()
    #
    main()
    #
    display.stop()