#!/usr/bin/python3
"""definening the function"""


def append_write(filename="", text=""):
    """function append the string at the end of the text file.
    Arg:
        and returns the number of the characters added"""

    with open(filename, mode='a', encoding='utf-8') as append_file:
        return append_file.write(text)
