#!/usr/bin/python3

"""defining the function that read text file"""


def read_file(filename=""):
    """intitialazing the function of the read_file that will read utf8"""
    with open(filename, encoding="utf-8") as read_file:
        print(read_file.read(), end="")
