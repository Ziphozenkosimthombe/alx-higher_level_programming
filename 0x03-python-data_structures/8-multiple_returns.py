#!/usr/bin/python3

"""returns a tuple with the length of a string and its first charecter"""


def multiple_returns(sentence):
    if sentence == 0:
        return 0, None
    return (len(sentence), sentence[0])
