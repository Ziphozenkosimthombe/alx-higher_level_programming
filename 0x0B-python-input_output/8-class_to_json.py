#!/usr/bin/python3
"""the modele of the python JSON serialization of an object"""


def class_to_json(obj):
    return obj.__dict__
