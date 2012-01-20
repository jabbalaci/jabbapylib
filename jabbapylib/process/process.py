#!/usr/bin/env python

"""
Interacting with processes.
* launch a new process
* launch a new process and get its output
* launch a new process in the background

# from jabbapylib.process import process
"""

import shlex
import psutil

from subprocess import call, Popen, PIPE, STDOUT


def get_simple_cmd_output(cmd, stderr=STDOUT):
    """Execute a simple external command and get its output.
    
    The command contains no pipes. Error messages are
    redirected to the standard output by default.
    """
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]


def get_cmd_output_input_from_stdin(cmd, input_file): #@ReservedAssignment
    """Execute an external command and get its output. The command
    receives its input_file from the stdin through a pipe.
    
    Example: 'echo test | grep es'."""
    args = shlex.split(cmd)
    p = Popen(args, stdout=PIPE, stdin=PIPE)    # | grep es
    p.stdin.write(input_file)                        # echo test |
    return p.communicate()[0]


def get_return_code_of_simple_cmd(cmd, stderr=STDOUT):
    """Execute a simple external command and return its exit status."""
    args = shlex.split(cmd)
    return call(args, stdout=PIPE, stderr=stderr)


def execute_cmd(cmd):
    """Execute a simple external command."""
    args = shlex.split(cmd)
    call(args)


def execute_cmd_in_background(cmd):
    """Execute a (shell) command in the background.
    
    Returns the process' pid."""
    #call("{0} &".format(cmd), shell=True)
    #http://stackoverflow.com/questions/1605520
    args = shlex.split(cmd)
    p = Popen(args)
    return p.pid
    
    
def get_process_list():
    """Get the list of running processes.
    
    Example:
        PROCNAME = "python.exe"
    
        for proc in psutil.process_iter():
            if proc.name == PROCNAME:
                proc.kill()
    """
    return psutil.process_iter()
    
#############################################################################
    
if __name__ == "__main__":
    print get_simple_cmd_output("echo -n Ubuntu")
    print get_cmd_output_input_from_stdin("grep es", "test")
    print get_return_code_of_simple_cmd("date")
    cmd = "/usr/bin/eog"
    print 'pid:', execute_cmd_in_background(cmd)
#    li = get_process_list()
#    for p in li:
#        print p.pid
    print '__END__'
