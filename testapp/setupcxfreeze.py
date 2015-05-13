from cx_Freeze import setup, Executable

import cx_Freeze.util

import sys, os, struct

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], \
    include_files = [], \
    compressed = True, silent = True,\
    optimize = 2, copy_dependent_files = True, \
    create_shared_zip = True, include_in_shared_zip = True)

executables = [
    Executable('app23.py',
        #base = 'Win32GUI',
        targetName = "app23"),
]

setup(name='app23',
      version = '0.1',
      description = 'Test app23',
      author = "romiq.kh@gmail.com",
      options = dict(build_exe = buildOptions),
      executables = executables)
