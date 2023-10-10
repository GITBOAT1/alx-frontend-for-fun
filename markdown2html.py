#!/usr/bin/python3
""" Write a script markdown2html.py that takes an
   argument 2 strings:
"""
import sys
import os


def markdown():
    """ convert form markdown arg
    """
    if len(sys.argv) == 3:
        if os.path.isfile(sys.argv[1]):
            exit(0)
        else:
            sys.stderr.write(f"Missing {markdown_file}\n")
            exit(1)

    else:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        exit(1)


if __name__ == "__main__":
    markdown()
