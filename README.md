jabbapylib
==========
A lightweight, general-purpose Python library.

* Author:  Laszlo Szathmary, 2011--2012 (<jabba.laci@gmail.com>)
* Website: <https://pythonadventures.wordpress.com/2011/09/06/jabbapylib/>
* GitHub:  <https://github.com/jabbalaci/jabbapylib>
* PyPI:    <http://pypi.python.org/pypi/jabbapylib/>

A small Python library that was primarily developed for my projects.
This library is quite specific for Linux, I've never tried
it under a different platform. Since this library is in an 
early stage, it is likely that it'll change a lot over time.
I plan to extend it with several new functionalities.

I've tested it with Python 2.7 under Ubuntu Linux.


Installation from PyPI:
-----------------------
The easiest way is via pip:

    $ sudo pip install jabbapylib

If you already have jabbapylib and you want to upgrade
to the latest version:

    $ sudo pip install jabbapylib -U

The library requires some Linux packages, their list can be
found in [sudo_apt-get_install.sh](https://github.com/jabbalaci/jabbapylib/blob/master/sudo_apt-get_install.sh).
Download the script and execute it:

    $ ./sudo_apt-get_install.sh

After the installation, you need to do the following steps if you want to
use all the funcionalities of the library:

1. I assume you use Firefox. In `~/.mozilla/firefox` put a symbolic link on 
   `~/.mozilla/firefox/XXXXXXXX.default/cookies.sqlite`.
2. Create the directory `~/tmp`.


Manual Installation:
--------------------
If you installed the library via pip (see the previous section), 
you can skip this section.

If you want to try the latest (development) version of jabbapylib,
you might want to download it directly from GitHub. Here is how to 
get it work in that case.

Create a folder and put this project in that folder.
In my case I put it in `~/python/lib/jabbapylib`. That is, I have this
hierarchy:

    ~/python/lib/jabbapylib/README.md              # this file
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

For installing the **dependencies** of this library,
execute the following scripts:

    $ ./sudo_apt-get_install.sh
    $ ./sudo_pip_install.sh

For running the **unit tests**, you need to do some
extra steps:

1. I assume you use Firefox. In `~/.mozilla/firefox` put a symbolic link on 
    `~/.mozilla/firefox/XXXXXXXX.default/cookies.sqlite`.
2. Create the directory `~/tmp`.
