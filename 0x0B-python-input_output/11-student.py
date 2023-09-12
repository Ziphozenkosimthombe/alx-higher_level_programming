#!/usr/bin/python3
"""defining the class"""


class Student:
    """initialazing the class of student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) is list and
                all(type(le) is str for le in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace the attributes of the student"""
        for a, j in json.items():
            setattr(self, a, j) 
