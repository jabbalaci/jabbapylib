#!/usr/bin/env python

"""
file system operations
"""

def read_first_line(input_file):
    """Read the first line of a file.
    
    Useful to read username, password, etc.
    Security tip: store such files on a Truecrypt volume."""
    f = open(input_file, 'r')
    line = f.readline().rstrip('\n')
    f.close()
    
    return line

############################################################################# 
 
if __name__ == "__main__":
    input = '/home/jabba/secret/project_euler/username.txt'
    print read_first_line(input)