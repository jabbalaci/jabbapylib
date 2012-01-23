#!/usr/bin/env python

"""
Primarily made for images but can be used with any kinds of files.
Image is a class to hold information about an image we want to download.

If you place a file or folder called "skip" in the target directory, the file
won't be downloaded.

# from jabbapylib.web.download import image
"""

SKIP = 'skip'

import os
import sys
from urlparse import urlparse

from jabbapylib.web import web
from jabbapylib.filesystem import fs

class Image:
    def __init__(self, base_dir, sub_dir, file_url):
        self.base_dir = base_dir
        self.sub_dir = sub_dir
        self.file_url = file_url
        self.readme = None
        
    def get_file_name(self):
        """Just the name of the file.
        
        Example: http://japancsaj.com/pic/rju_ri/rju_ri_9.jpg => rju_ri_9.jpg ."""
        return os.path.split(urlparse(self.file_url)[2])[1]
        
    def get_local_dir(self):
        """The directory where the image is to be saved."""
        return os.path.join(self.base_dir, self.sub_dir)
        
    def get_local_path(self):
        """Local path of the file."""
        return os.path.join(self.get_local_dir(), self.get_file_name())
    
    def get_skip_path(self):
        """Path of the file whose presence means not to download this file."""
        return os.path.join(self.get_local_dir(), SKIP)
    
    def exists(self):
        """Does this file exist?"""
        return os.path.isfile(self.get_local_path())
    
    def make_dirs(self):
        """Make all the directories for the file.""" 
        d = self.get_local_dir()
        if not os.path.exists(d):
            try:
                os.makedirs(d)
            except:
                return False
            
        return True     # existed or managed to create, i.e. everything is OK
    
    def get_readme_path(self):
        """Path of a README file.
        
        You might want to save the file with some description too."""
        return os.path.join(self.get_local_dir(), 'README')
    
    def save_readme(self):
        """Save the README file."""
        readme = self.get_readme_path()
        if not os.path.isfile(readme):
            f = open(readme, 'w')
            f.write(self.readme)
            f.close()
    
    def download(self, warning=True):
        """Download yourself."""
        if os.path.exists(self.get_skip_path()):
            return False
        
        # else
        if not self.exists():
            if self.make_dirs():
                obj = web.get_page(self.file_url, user_agent=True, referer=True)
                fs.store_content_in_file(obj, self.get_local_path())
        
        ok = self.exists()
        if not ok and warning:
            print >>sys.stderr, "# warning: couldn't download {url}.".format(url=self.file_url)
            
        if self.readme:
            self.save_readme()
            
        return ok
        
    
#############################################################################
    
if __name__ == "__main__":
    img = Image('/trash/download', '2011-10-29', 'http://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Bodiam-castle-10My8-1197.jpg/300px-Bodiam-castle-10My8-1197.jpg')
    print img.get_local_path()
    print "exists:", img.exists()
    img.download()
