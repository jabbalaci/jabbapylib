#!/usr/bin/env python

"""
Interacting with processes.
* launch a new process
* launch a new process and get its output
* launch a new process in the background
"""

import shlex

from subprocess import call, Popen, PIPE, STDOUT


def get_simple_cmd_output(cmd, stderr=STDOUT):
    """Execute a simple external command and get its output.
    
    The command contains no pipes. Error messages are
    redirected to the standard output by default.
    """
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]


def get_cmd_output_input_from_stdin(cmd, input): #@ReservedAssignment
    """Execute an external command and get its output. The command
    receives its input from the stdin through a pipe.
    
    Example: 'echo test | grep es'."""
    args = shlex.split(cmd)
    p = Popen(args, stdout=PIPE, stdin=PIPE)    # | grep es
    p.stdin.write(input)                        # echo test |
    return p.communicate()[0]


def get_return_code_of_simple_cmd(cmd, stderr=STDOUT):
    """Execute a simple external command and return its exit status."""
    args = shlex.split(cmd)
    return call(args, stdout=PIPE, stderr=stderr)


def execute_cmd_in_background(cmd):
    """Execute a (shell) command in the background."""
    call("{0} &".format(cmd), shell=True)
    
#############################################################################
    
if __name__ == "__main__":
    #cmd = "/usr/bin/eog"
    #execute_cmd_in_background(cmd)
    print get_cmd_output_input_from_stdin("grep es", "test")