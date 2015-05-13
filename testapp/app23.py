#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

if os.environ.get("TESTBAKED"):
    import gettextbaked as gettext
else:
    import gettext
    gettext.bindtextdomain("app23", 
        os.path.join(os.path.dirname(__file__), "locale"))

gettext.textdomain("app23")
_ = gettext.gettext
gettext.install("app23")

def main():
    print(_("Test context"))

    tr = gettext.translation("app23", fallback = True)

    for i in range(11 if len(sys.argv) < 2 else int(sys.argv[1])):
        print(gettext.ngettext("{} apple", "{} apples", i).format(i))
    
if __name__ == "__main__":
    sys.exit(main())

