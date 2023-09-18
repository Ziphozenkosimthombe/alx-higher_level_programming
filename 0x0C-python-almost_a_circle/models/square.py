#!/usr/bin/python3
"""importing """

from models.rectangle import Rectangle

"""defining the class Square"""


class Square(Rectangle):
    """intialazing the class square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """the class constructors"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        for i, arg in enumerate(args):

            if i == 0:
                self.id = args[0]

            elif i == 1:
                self.size = args[1]

            elif i == 2:
                self.x = args[2]

            elif i == 3:
                self.y = args[3]

        if (kwargs):

            if 'id' in kwargs:
                self.id = kwargs['id']

            if 'size' in kwargs:
                self.size = kwargs['size']

            if 'x' in kwargs:
                self.x = kwargs['x']

            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        dict_list_square = {
                'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y
                }
        return dict_list_square
