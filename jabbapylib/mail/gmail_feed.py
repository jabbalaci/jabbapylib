#!/usr/bin/env python

"""
Gmail has an atom feed at https://mail.google.com/mail/feed/atom
that lists unread messages. We return this feed with this script.

from http://stackoverflow.com/questions/1777081/how-to-auto-log-into-gmail-atom-feed-with-python

# import jabbapylib.mail.gmail_feed
"""

import urllib2

FEED_URL = 'https://mail.google.com/mail/feed/atom'


def get_unread_msgs(user, passwd):
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm='New mail feed',
        uri='https://mail.google.com',
        user='{user}@gmail.com'.format(user=user),
        passwd=passwd
    )
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)
    feed = urllib2.urlopen(FEED_URL)
    return feed.read()

#############################################################################

if __name__ == "__main__":
    import getpass
    
    user = raw_input('Username: ')
    passwd = getpass.getpass('Password: ')
    print get_unread_msgs(user, passwd)
