#!/usr/bin/python3
"""returns a keywith the biggest integer value"""


def best_score(a_dictionary):
    if a_dictionary:
        return (max(a_dictionary, key=a_dictionary.get))
    return None
