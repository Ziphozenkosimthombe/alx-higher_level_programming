#!/usr/bin/python3
"""defining the text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """inserting each text after line containing a given string in the file"""
    text = ''
    with open(filename) as a:
        for line in a:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as w:
        w.write(text)
