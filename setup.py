#!/usr/bin/env python

"""
jabbapylib
----------

A lightweight, general-purpose Python library.

Links
`````

* `website <https://github.com/jabbalaci/jabbapylib>`_
"""

from setuptools import setup, find_packages #@UnresolvedImport

import jabbapylib.config as cfg


setup(
    name='jabbapylib',
    packages = find_packages(exclude=['demos', 'dist', 'tests']),
    version=cfg.__version__,
    description='A lightweight, general-purpose Python library',
    long_description=__doc__,
    author='Laszlo Szathmary',
    author_email='jabba.laci@gmail.com',
    url='https://github.com/jabbalaci/jabbapylib',
    keywords = ['jabba', 'library', 'scraper', 'api'],
    license='GPLv3',
    platforms='Linux',
    install_requires=[
        'html5lib',
        'psutil',
        'pytest',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Operating System :: POSIX :: Linux',
		'Topic :: Utilities',
    ],
)
