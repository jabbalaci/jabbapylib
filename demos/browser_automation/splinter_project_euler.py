#!/usr/bin/env python

"""
splinter

http://splinter.cobrateam.info
"""

from splinter.browser import Browser
from jabbapylib.filesystem import fs

PE_LOGIN = 'http://projecteuler.net/login'
PE_COUNTRIES = 'http://projecteuler.net/countries'

USERNAME = fs.read_first_line('/home/jabba/secret/project_euler/username.txt')
PASSWORD = fs.read_first_line('/home/jabba/secret/project_euler/password.txt')

def main():
#    browser = Browser('chrome')
    browser = Browser()
    browser.visit(PE_LOGIN)
    
    browser.fill('username', USERNAME)
    browser.fill('password', PASSWORD)
    button = browser.find_by_name('login')
    button.click()

    browser.visit(PE_COUNTRIES)
       
    f = open("/tmp/stat.html", "w")
    print >>f, browser.html
    f.close()
    
    browser.quit()

    print '__END__'

#############################################################################

if __name__ == "__main__":
    main()