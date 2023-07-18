#!/usr/bin/python3
"""
Test case for class Rectangle
"""


import sys
import pep8
import os
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


class TestPep8(unittest.TestCase):
    """Tests pep8 guidelines for models/rectangle.py"""
    def test_pep8(self):
        """Tests pep8"""
        style = pep8.StyleGuide(quiet=False)
        results = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        results += style.check_files(files).total_errors
        self.assertEqual(results, 0, 'Fix pep8')


class TestRectangle(unittest.TestCase):
    """Tests models/rectangle.py"""
    def test_default_attr(self):
        """Tests the attributes by default"""
        rec = Rectangle(5, 6)
        self.assertTrue(rec.width == 5)
        self.assertTrue(rec.height == 6)
        self.assertTrue(rec.x == 0)
        self.assertTrue(rec.y == 0)
        self.assertTrue(rec.id is not None)

    def test_args(self):
        """Tests the args given to rep"""
        rec = Rectangle(2, 3, 4, 5, 6)
        self.assertTrue(rec.width == 2)
        self.assertTrue(rec.height == 3)
        self.assertTrue(rec.x == 4)
        self.assertTrue(rec.y == 5)
        self.assertTrue(rec.id == 6)

    def test_more_args(self):
        """Tests if more arguments passed"""
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, 5, 6, 7, 8)

    def test_less_args(self):
        """Tests few arguments passed"""
        with self.assertRaises(TypeError):
            Rectangle(4)

    def test_no_args(self):
        """Tests when no args passed"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_zero_height(self):
        """Tests whn the height is zero"""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_private_att_access(self):
        """Tests access of private attributes"""
        with self.assertRaises(AttributeError):
            Rectangle.__width
            Rectangle.__height
            Rectangle.__x
            Rectangle.__y

    def test_class(self):
        """Tests class is indeed Rectangle"""
        self.assertTrue(Rectangle(5, 6), self.__class__ == Rectangle)

    def test_att_values(self):
        """Tests the values given for the
        attributes and error raised where necessary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 3, 4, 5, 6)
            Rectangle([2, 3], 4, 5, 6, 7)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (3, 5), 4, 5, 7)
            Rectangle(2, {6: 7}, 5, 6, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None, 3, 4)
            Rectangle(1, 2, (ten), 3, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "one", 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2, 3, 4, 6)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -4, 5, 6, 7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 3, -2, 4, 6)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(20, 30, 25, -45, 60)

    def test_rec_area(self):
        """Tests the area of the rectangle"""
        self.assertEqual(Rectangle(4, 5).area(), 20)
        self.assertEqual(Rectangle(2, 3, 0, 0, 7).area(), 6)
        self.assertEqual(Rectangle(8, 20, 3, 4, 76).area(), 160)
        self.assertEqual(Rectangle(4, 7, 2, 1).area(), 28)

    def test_display(self):
        """Tests display"""
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3).display()
            b = bufr.getvalue()
        self.assertEqual(b, '#####\n#####\n#####\n')
        with StringIO() as bufr, redirect_stdout(bufr):
            Rectangle(5, 3, 1, 2).display()
            b = bufr.getvalue()
        self.assertEqual(b, '\n\n #####\n #####\n #####\n')

    def test_display_without_cordinates(self):
        """Tests without y coordinate"""
        with StringIO() as buff, redirect_stdout(buff):
            Rectangle(5, 3, 1).display()
            b = buff.getvalue()
            self.assertEqual(b, ' #####\n #####\n #####\n')

    def test_str(self):
        """Tests how it prints out the rectangle"""
        rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rec), '[Rectangle] (5) 3/4 - 1/2')

    def test_args_update(self):
        """Test method: update(*args)"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 10, 10, 10, 10)
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (10) 10/10 - 10/10')
        r.update(99)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 10/10')
        r.update(99, 1)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/10')
        r.update(99, 1, 2)
        self.assertEqual(str(r), '[Rectangle] (99) 10/10 - 1/2')
        r.update(99, 1, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (99) 3/4 - 1/2')

    def test_invalid_args_update(self):
        """Test invalid *args"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(99, 1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(99, 1, 2, 3, "string")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(99, 1, 2, 3, -99)

    def test_kwargs_update(self):
        """Test method: update(*kwargs)"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=55)
        self.assertEqual(str(r), '[Rectangle] (55) 3/4 - 1/2')
        r.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(r), '[Rectangle] (44) 770/880 - 990/2')

    def test_invalid_kwargs_update(self):
        """Test mixture of valid and invalid *kwargs"""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=44, x=770, y=880, width=990)
        self.assertEqual(str(r), '[Rectangle] (44) 770/880 - 990/2')
        r.update(nokey=1000, invalid=2000, testing=3000, id=4000)
        self.assertEqual(str(r), '[Rectangle] (4000) 770/880 - 990/2')
