#!/usr/bin/python3
"""importing unittest module"""
import unittest
from models.square import Square

"""defining the TestSquare class that inherits from unittest.TestCase"""


class TestSquare(unittest.TestCase):
    """testing the Square class"""

    def test_init(self):
        """testing the __init__ method"""
        s1 = Square(5, 2, 3, 4)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 4)

    def test_area(self):
        """testing the area method"""
        s2 = Square(10)
        self.assertEqual(s2.area(), 100)

    def test_str(self):
        """testing the __str__ method"""
        s7 = Square(2, 3, 4, 5)
        self.assertEqual(str(s7), "[Square] (5) 3/4 - 2")

    def test_size(self):
        """testing the size property"""
        s8 = Square(8)
        self.assertEqual(s8.size, 8)
        s8.size = 9
        self.assertEqual(s8.size, 9)

    def test_size_setter(self):
        """testing the size setter method"""
        s9 = Square(7)
        s9.size = 8
        self.assertEqual(s9.size, 8)
        self.assertEqual(s9.width, 8)
        self.assertEqual(s9.height, 8)

    def test_update(self):
        """testing the update method with args and kwargs"""
        s10 = Square(5)
        s10.update(6, 7, 8, 9)
        self.assertEqual(s10.id, 6)
        self.assertEqual(s10.size, 7)
        self.assertEqual(s10.x, 8)
        self.assertEqual(s10.y, 9)
        s10.update(size=10, y=11, x=12, id=13)
        self.assertEqual(s10.id, 13)
        self.assertEqual(s10.size, 10)
        self.assertEqual(s10.x, 12)
        self.assertEqual(s10.y, 11)

    def test_to_dictionary(self):
        """testing the to_dictionary method"""
        s11 = Square(3, 4, 5, 6)
        d11 = {'id': 6, 'size': 3, 'x': 4, 'y': 5}
        self.assertDictEqual(s11.to_dictionary(), d11)


if __name__ == '__main__':
    unittest.main()
