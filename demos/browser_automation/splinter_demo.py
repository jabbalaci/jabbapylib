#!/usr/bin/env python

"""
splinter

http://splinter.cobrateam.info
"""

def main():
    from splinter.browser import Browser

    browser = Browser()
    browser.visit('http://google.com')
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    browser.find_by_css('.lsb').first.click()
    
    if browser.is_text_present('splinter.cobrateam.info'):
        print "Yes, the official website was found!"
    else:
        print "No, it wasn't found... We need to improve our SEO techniques"
    
    #browser.execute_script("var win = window.open(); win.document.write('<html><head><title>Generated HTML of  ' + location.href + '</title></head><pre>' + document.documentElement.innerHTML.replace(/&/g, '&amp;').replace(/</g, '&lt;') + '</pre></html>'); win.document.close(); void 0;")
    
    browser.quit()

#############################################################################

if __name__ == "__main__":
    main()