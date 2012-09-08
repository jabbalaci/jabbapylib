#!/usr/bin/env python

"""
Simple API for:
* posting links to reddit
* commenting on a post

This requires that you have a reddit account. Put your username and
password in the following files:
* ~/reddit_username.txt
* ~/reddit_password.txt

To use RedBot, just make a subclass of it and give it a cool name:

class HyperBot(RedBot):
    def __init__(self):
        super(HyperBot, self).__init__()
        self.name = 'HyperBot'
        
Now you are ready to flood reddit :)

# from jabbapylib.reddit import red
"""

import sys
import reddit
from jabbapylib.filesystem import fs
from jabbapylib.platform import platform

USERNAME_TXT = '{home}/reddit_username.txt'.format(home=platform.get_home_dir())
PASSWORD_TXT = '{home}/reddit_password.txt'.format(home=platform.get_home_dir())
#
USERNAME = fs.read_first_line(USERNAME_TXT)
PASSWORD = fs.read_first_line(PASSWORD_TXT)


class RedBot(object):
    def __init__(self):
        self.name = 'RedBot'
        self.username = USERNAME
        self.password = PASSWORD
        #
        self.r = reddit.Reddit(user_agent=self.name)
        self.r.login(username=self.username, password=self.password)
        self.last_post = None   # Submission object
        self.permalink = None   # URL of the last post
        
    def submit_link(self, url, subreddit, title):
        """
        The return value (res) is a Submission object or None.
        URL of the newly created post: res.permalink
        """
        try:
            self.last_post = self.r.submit(subreddit, title, url=url)
            self.permalink = self.last_post.permalink
            print '# url to send: {url}'.format(url=url)
            print '# submitted to: {pl}'.format(pl=self.permalink)
            return self.last_post
        except:
            print >>sys.stderr, "Warning: couldn't submit {url}".format(url=url)
            return None
        
    def add_comment(self, comment):
        if self.last_post:
            self.last_post.add_comment(comment)
            print '# comment added'

#############################################################################

if __name__ == "__main__":
# here is how to use it:
#    url = '...'
#    subreddit = '...'
#    title = "..."
#    comment = '...'
#    r = RedBot()
#    r.submit_link(url, subreddit, title)
#    r.add_comment(comment)
    pass
