#!/usr/bin/python3
"""defining the function"""


def write_file(filename="", text=""):
    """initialazing the filename and the text.
    Arg:
        function write the str to the text file.
    Return:
            return the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file_write:
        return file_write.write(text)
