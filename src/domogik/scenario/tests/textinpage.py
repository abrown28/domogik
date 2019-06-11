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

@author: Maxence Dunnewind <maxence@dunnewind.net>
@copyright: (C) 2007-2009 Domogik project
@license: GPL(v3)
@organization: Domogik
"""

from domogik.scenario.tests.abstract import AbstractTest
from time import sleep

class TextInPageTest(AbstractTest):
    """ Simple test to check if a word is contained in an url
    """

    def __init__(self, log = None, trigger = None, cond=None, params=None):
        AbstractTest.__init__(self, log, trigger, cond, params)
        self.set_outputCheck(["Boolean"])
        self.set_description("Check if a web page contains some text")
        self.add_parameter("text", "text.TextParameter")
        self.add_parameter("url", "url_value.UrlParameter")

    def evaluate(self):
        """ Evaluate if the text appears in the content of the page referenced by url
        """
        p = self.get_raw_parameters()
        u = p["url"]
        t = p["text"]
        if u.evaluate() == None or t.evaluate() == None:
            return None
        else:
            res = t.evaluate() in u.evaluate().decode('utf-8')
            return res


if __name__ == "__main__":
    TEST = None
    import logging

    def mytrigger(test):
        print("Trigger called by test {0}, refreshing state".format(test))
        st = TEST.evaluate()
        print("state is {0}".format(st))

    FORMAT = "%(asctime)-15s %(message)s"
    logging.basicConfig(format=FORMAT)
    TEST = TextInPageTest(logging, trigger = mytrigger)
    print("getting parameters")
    p = TEST.get_parameters()
    print(p)
    print("Trying to evaluate : {0}".format(TEST.evaluate()))
    print("set data for parameters")
    data = { "url": { "urlpath" : "http://people.dunnewind.net/maxence/domogik/test.txt",
                    "interval": "5"
    },
    "text": {
        "text" : "this text does not exists"
    }
    }
    TEST.fill_parameters(data)
    print("I sleep 5s")
    sleep(5)
    print("Trying to evaluate : {0}".format(TEST.evaluate()))
    print("updating with good text")
    data = { "url": { "urlpath" : "http://people.dunnewind.net/maxence/domogik/test.txt",
                    "interval": "5"
    },
    "text": {
        "text" : "randomtext"
    }
    }
    print("====")
    TEST.fill_parameters(data)
    print("====")
    print("I sleep 5s")
    sleep(5)
    print("Trying to evaluate : {0}".format(TEST.evaluate()))
    TEST.destroy()
