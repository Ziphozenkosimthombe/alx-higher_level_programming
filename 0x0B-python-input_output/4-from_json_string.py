#!/usr/bin/python3

"""import the module of json"""
import json


def from_json_string(my_str):
    """function that return an object represented by a JSON string"""
    return json.loads(my_str)
