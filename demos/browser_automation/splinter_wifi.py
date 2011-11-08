#!/usr/bin/env python

"""
login to my wifi
"""

from splinter.browser import Browser
from time import sleep

URL = 'https://controller...'

def main():
    br = Browser('chrome')
    br.visit(URL)
    sleep(3)
    if br.is_text_present('Connection', wait_time=7):
        br.fill('login', '...')
        br.fill('password', '...')
        br.find_by_css('#logonForm_connect_button').first.click()
        
#############################################################################

if __name__ == "__main__":
    main()