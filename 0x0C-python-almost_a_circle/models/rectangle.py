#!/usr/bin/python3
"""importing the mosule of the Base"""

from models.base import Base


class Rectangle(Base):
    """defining the  rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of the object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if (type(width) is not int):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @height.setter
    def height(self, height):
        if (type(height) is not int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        if (type(x) is not int):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @y.setter
    def y(self, y):
        if (type(y) is not int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        return self.__height * self.__width

    def display(self):
        for a in range(self.y):
            print("")

        for rows in range(self.__height):

            for b in range(self.x):
                print(" ", end="")

            for columns in range(self.__width):
                print("#", end="")

            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        for i, arg in enumerate(args):
            if i == 0:
                self.id = args[0]

            elif i == 1:
                self.__width = args[1]

            elif i == 2:
                self.__height = args[2]

            elif i == 3:
                self.__x = args[3]

            elif i == 4:
                self.__y = args[4]

        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']

            if 'width' in kwargs:
                self.__width = kwargs['width']

            if 'height' in kwargs:
                self.__height = kwargs['height']

            if 'x' in kwargs:
                self.__x = kwargs['x']

            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of Rectangle"""
        dictionary_list = {
                'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x,
                'y': self.__y
                }
        return dictionary_list

    def __eq__(self, other):
        return (self.width == other.width and
                self.height == other.height and
                self.x == other.x and
                self.y == other.y and
                self.id == other.id)
