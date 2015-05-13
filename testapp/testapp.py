#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

if os.environ.get("TESTBAKED"):
    import gettextbaked as gettext
else:
    import gettext
    gettext.bindtextdomain("testapp", 
        os.path.join(os.path.dirname(__file__), "locale"))

gettext.textdomain("testapp")
_ = gettext.gettext

def main():
    print(_("Hello from Test program"))
    print(_("Arguments: ({})").format(len(sys.argv) - 1))
    for idx, arg in enumerate(sys.argv[1:]):
        print(_("%d) %s") % (idx + 1, arg))
    # print(_("")) # Empty string bound to settings
    print(_("Environment variables:"))
    for idx, (key, value) in enumerate(os.environ.items()):
        print(_("{:d}) {} = {}").format(idx + 1, key, repr(value)))
    print(_("End of output"))
    
if __name__ == "__main__":
    sys.exit(main())

