#!/usr/bin/python3
"""importing the json module """
import json


def save_to_json_file(my_obj, filename):
    """function that return an object to a text file using a JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as a:
        json.dump(my_obj, a)
