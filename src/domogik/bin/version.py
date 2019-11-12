#!/usr/bin/python
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

Plugin purpose
=============

- Display Domogik release

Implements
==========




@author: Friz <fritz.smh@gmail.com>
@copyright: (C) 2007-2012 Domogik project
@license: GPL(v3)
@organization: Domogik
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from domogik.bin.admin import REST_API_VERSION
#import domogik.admin.rest
import sys
import os
from subprocess import Popen, PIPE

def rest_status_dmg_release():
    """ Return Domogik release
    """
    __import__("domogik")
    global_release = sys.modules["domogik"].__version__
    return global_release


def main():
    print(u"REST_API_release : {0}".format(REST_API_VERSION))
    print(u"Domogik_release : {0}".format(rest_status_dmg_release()))
    print(u"Sources_release : {0}".format(rest_status_dmg_release()))


if __name__ == "__main__":
    main()

