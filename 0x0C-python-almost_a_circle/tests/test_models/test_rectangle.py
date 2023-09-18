#!/usr/bin/python3
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tect cases for the rectangle class"""

    def setUp(self):
        """Set up the test environment"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """Test the initialization of a Rectangle object"""
        r1 = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1)

    def test_init_errors(self):
        """Test the errors raised by invalid arguments"""
        with self.assertRaises(TypeError):
            r2 = Rectangle("a", 10)
            with self.assertRaises(ValueError):
                r3 = Rectangle(-5, 10)

    def test_width_property(self):
        """Test the width property of a Rectangle object"""
        r4 = Rectangle(10, 20)
        self.assertEqual(r4.width, 10)
        r4.width = 15
        self.assertEqual(r4.width, 15)
        with self.assertRaises(TypeError):
            r4.width = "a"
        with self.assertRaises(ValueError):
            r4.width = -5

    def test_height_property(self):
        """Test the height property of a Rectangle object"""
        r5 = Rectangle(10, 20)
        self.assertEqual(r5.height, 20)
        r5.height = 25
        self.assertEqual(r5.height, 25)
        with self.assertRaises(TypeError):
            r5.height = "b"
        with self.assertRaises(ValueError):
            r5.height = -10

    def test_x_property(self):
        """Test the x property of a Rectangle object"""
        r6 = Rectangle(10, 20)
        self.assertEqual(r6.x, 0)
        r6.x = 5
        self.assertEqual(r6.x, 5)
        with self.assertRaises(TypeError):
            r6.x = "c"
        with self.assertRaises(ValueError):
            r6.x = -15

    def test_y_property(self):
        """Test the y property of a Rectangle object"""
        r7 = Rectangle(10, 20)
        self.assertEqual(r7.y, 0)
        r7.y = 10
        self.assertEqual(r7.y, 10)
        with self.assertRaises(TypeError):
            r7.y = "d"
        with self.assertRaises(ValueError):
            r7.y = -20

    def test_width_setter(self):
        """Test the width setter of a Rectangle object"""
        r8 = Rectangle(10, 20)
        r8.width = 15
        self.assertEqual(r8.width, 15)
        with self.assertRaises(TypeError):
            r8.width = "a"
        with self.assertRaises(ValueError):
            r8.width = -5

    def test_height_setter(self):
        """Test the height setter of a Rectangle object"""
        r9 = Rectangle(10, 20)
        r9.height = 25
        self.assertEqual(r9.height, 25)
        with self.assertRaises(TypeError):
            r9.height = "b"
        with self.assertRaises(ValueError):
            r9.height = -10

    def test_x_setter(self):
        """Test the x setter of a Rectangle object"""
        r10 = Rectangle(10, 20)
        r10.x = 5
        self.assertEqual(r10.x, 5)
        with self.assertRaises(TypeError):
            r10.x = "c"
        with self.assertRaises(ValueError):
            r10.x = -15

    def test_y_setter(self):
        """Test the y setter of a Rectangle object"""
        r11 = Rectangle(10, 20)
        r11.y = 10
        self.assertEqual(r11.y, 10)
        with self.assertRaises(TypeError):
            r11.y = "d"
        with self.assertRaises(ValueError):
            r11.y = -20

    def test_area(self):
        """Test the area method of a Rectangle object"""
        r12 = Rectangle(10, 20)
        self.assertEqual(r12.area(), 200)
        r12.width = 15
        r12.height = 25
        self.assertEqual(r12.area(), 375)

    def test_display(self):
        """Test the display method of a Rectangle object"""
        r13 = Rectangle(10, 20, 5, 10)
        output = io.StringIO()
        sys.stdout = output
        r13.display()
        sys.stdout = sys.__stdout__
        expected_output = "\n" * 10
        expected_output += " " * 5 + "#" * 10 + "\n"
        expected_output += (" " * 5 + "#" * 10 + "\n") * 19
        self.assertEqual(output.getvalue(), expected_output)

    def test_str(self):
        """Test the __str__ method of a Rectangle object"""
        r14 = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(str(r14), "[Rectangle] (1) 5/10 - 10/20")
        r14.width = 15
        r14.height = 25
        r14.x = 10
        r14.y = 15
        r14.id = 2
        self.assertEqual(str(r14), "[Rectangle] (2) 10/15 - 15/25")

    def test_update(self):
        """Test the update method of a Rectangle object"""
        r15 = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r15.width, 10)
        self.assertEqual(r15.height, 20)
        self.assertEqual(r15.x, 5)
        self.assertEqual(r15.y, 10)
        self.assertEqual(r15.id, 1)

        r15.update(2, 15, 25, 10, 15)
        self.assertEqual(r15.width, 15)
        self.assertEqual(r15.height, 25)
        self.assertEqual(r15.x, 10)
        self.assertEqual(r15.y, 15)
        self.assertEqual(r15.id, 2)

        r15.update(id=3, width=20, height=30, x=15, y=20)
        self.assertEqual(r15.width, 20)
        self.assertEqual(r15.height, 30)
        self.assertEqual(r15.x, 15)
        self.assertEqual(r15.y, 20)
        self.assertEqual(r15.id, 3)

    def test_to_dictionary(self):
        """Test the to_dictionary method of a Rectangle object"""
        r16 = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(
                r16.to_dictionary(),
                {'id': 1, 'width': 10, 'height': 20, 'x': 5, 'y': 10})
        r16.width = 15
        r16.height = 25
        r16.x = 10
        r16.y = 15
        r16.id = 2
        self.assertEqual(
                r16.to_dictionary(),
                {'id': 2, 'width': 15, 'height': 25, 'x': 10, 'y': 15})

    def test_eq(self):
        """Test the __eq__ method of a Rectangle object"""
        r17 = Rectangle(10, 20, 5, 10, 1)
        r18 = Rectangle(10, 20, 5, 10, 1)
        r19 = Rectangle(15, 25, 10, 15, 2)
        self.assertTrue(r17 == r18)
        self.assertFalse(r17 == r19)


if __name__ == '__main__':
    unittest.main()
