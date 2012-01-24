jabbapylib
==========

A small Python library that I use for my projects.

* Author:  Laszlo Szathmary, 2011--2012 (<jabba.laci@gmail.com>)
* Website: <https://pythonadventures.wordpress.com/2011/09/06/jabbapylib/>
* GitHub:  <https://github.com/jabbalaci/jabbapylib>


This library is quite specific for Linux, I've never tried
it under a different platform. Since this library is in an 
early stage, it is likely that it'll change a lot over time.
I plan to extend it with several new functionalities.

I've tested it with Python 2.7 under Ubuntu Linux.


Usage:
------

Create a folder and put this project in that folder.
In my case I put it in `~/python/lib/jabbapylib`. That is, I have this
hierarchy:

    ~/python/lib/jabbapylib/README.md    # this file
    ~/python/lib/jabbapylib/jabbapylib/config.py

etc.

Then add this folder to `PYTHONPATH` in your `~/.bashrc` file:

    PYTHONPATH=$PYTHONPATH:$HOME/python/lib/jabbapylib
    export PYTHONPATH

Source `.bashrc` (or open a new terminal), start the Python
shell and try this:

    >>> from jabbapylib.say.hello import hi
    >>> hi()

If you see a greetings, jabbapylib is set up properly :)


Requirements:
-------------

For installing the dependencies of this library,
execute the following scripts:

    $ ./sudo_apt-get_install.sh
    $ ./sudo_pip_install.sh


Unit tests:
-----------

For running the unit tests, you need to do some
extra steps:

1. I assume you use Firefox. In `~/.mozilla/firefox` put a symbolic link on 
    `~/.mozilla/firefox/XXXXXXXX.default/cookies.sqlite`.
2. Create the directory `~/tmp`.

