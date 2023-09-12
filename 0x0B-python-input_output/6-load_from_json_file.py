#!/usr/bin/python3
"""importing the jsom module"""
import json


def load_from_json_file(filename):
    """function that create an object from a JSON file"""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
