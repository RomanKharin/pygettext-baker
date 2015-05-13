#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

if hasattr(sys, 'frozen') or os.environ.get("TESTBAKED"):
    import gettextbaked as gettext
    tr = gettext.translation("app23", fallback = True)
else:
    import gettext
    tr = gettext.translation("app23", fallback = True, localedir =
        os.path.join(os.path.dirname(__file__), "locale"))
tr.install()

def main():

    print(_("Test context"))

    for i in range(11 if len(sys.argv) < 2 else int(sys.argv[1])):
        print(tr.ngettext("{} apple", "{} apples", i).format(i))
    
if __name__ == "__main__":
    sys.exit(main())

