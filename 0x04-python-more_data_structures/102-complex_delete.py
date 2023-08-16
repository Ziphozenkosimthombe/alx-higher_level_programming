#!/usr/bin/python3
"""deletes keys with a specific value in a dictionary"""


def complex_delete(a_dictionary, value):
    listForKeys = list(a_dictionary.keys())
    for dictionaryValue in listForKeys:
        if value == a_dictionary.get(dictionaryValue):
            del a_dictionary[dictionaryValue]
    return a_dictionary
