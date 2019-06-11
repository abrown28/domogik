#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" This file is part of B{Domogik} project (U{http://www.domogik.org}).

License
=======

B{Domogik} is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

B{Domogik} is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Domogik. If not, see U{http://www.gnu.org/licenses}.

Module purpose
==============

Help to manage Domogik installation

Implements
==========


@author: Domogik project
@copyright: (C) 2007-2019 Domogik project
@license: GPL(v3)
@organization: Domogik
"""

import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

mysql = 'pymysql'
magic = 'python-magic >= 0.4.3'

import pkg_resources
dists = [d for d in pkg_resources.working_set]
for mod in dists:
    if ( mod.key == 'mysql-python' ):
        mysql = 'mysql-python'
    if ( mod.key == 'magic-file-extensions' ):
        magic = 'magic-file-extensions'

print(u"******************************************")
print(u"use: {0}".format(mysql))
print(u"use: {0}".format(magic))
print(u"******************************************")

setup(
    name = 'Domogik',
    version = '0.6.1',
    url = 'http://www.domogik.org/',
    description = 'OpenSource home automation software',
    author = 'Domogik team',
    author_email = 'domogik-general@lists.labs.libre-entreprise.org',
    install_requires=['setuptools',
          ],
    zip_safe = False,
    license = 'GPL v3',
    #include_package_data = True,
    packages = find_packages('src', exclude=["mpris"]),
    package_dir = { '': 'src' },
    test_suite = 'domogik.tests',
    package_data = {},
    scripts=[],
    entry_points = {
        'console_scripts': [
        """
            dmg_manager = domogik.bin.manager:main
            dmg_send = domogik.bin.send:main
            dmg_dump = domogik.bin.dump_xpl:main
            dmg_version = domogik.bin.version:main
            dmg_hub = domogik.bin.hub:main
            dmg_package = domogik.bin.package:main
            dmg_testrunner = domogik.tests.bin.testrunner:main
            dmg_cron = domogik.bin.cron:main
            dmg_review = domogik.tools.packages.review:main
        """
        ]
    },
    classifiers=[
        "Topic :: Home Automation",
        "Environment :: No Input/Output (Daemon)",
        "Programming Language :: Python3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English"
    ]
)

