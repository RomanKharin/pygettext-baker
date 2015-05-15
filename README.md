# pygettext-baker
Bake .po/.mo data into .py files for portable applications

  Author: romiq.kh@gmail.com

  Version: 0.1

Usage:

```
pygettextbaker.py /path/to/mofiles /path/to/created/gettextbaked
```

This create new python module with `__init__.py` and `lang.py` for every found
language .mo file. If there are only `.po` file or `.mo` file are older than
`.po`, `msgfmt` will be called for compilation.

Created module can be used as following:

```python
    import gettextbaked as gettext
    tr = gettext.translation("domain", fallback = True)
    _ = tr.gettext
```

More examples are in `testapp` folder.

Module heavily based on Python's `gettext.py` module, with copying some code 
from it.
