#!/usr/bin/env python3

# creator.py

import sys
from src import run

if __name__ == "__main__":

    if (sys.version_info.major, sys.version_info.minor) != (3, 7):
        print(
            """You must use python 3.7.3 or greater to run this app.
            ~
            Type "python3.7 creator.py [project_name]" or if not installed
            got to python.org and download the interpreter."""
        )
        exit()
    else:
        del sys

        run()
