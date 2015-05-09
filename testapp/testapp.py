#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import gettext

gettext.bindtextdomain("default", 
    os.path.join(os.path.dirname(__file__), "locale"))
gettext.textdomain("default")
_ = gettext.gettext

def main():
    print(_("Hello from Test program"))
    print(_("Arguments: ({})").format(len(sys.argv) - 1)
    for idx, arg in enumerate(sys.argv[1:]):
        print(_("%d): %s") % (idx + 1, arg))
    print(_(""))
    for idx, (key, value) in os.env.items():
        print(_("{:d}) {} = {}").format(idx, key, value))
    print(_("End on output"))    
    
if __name__ == "__main__":
    sys.exit(main())

