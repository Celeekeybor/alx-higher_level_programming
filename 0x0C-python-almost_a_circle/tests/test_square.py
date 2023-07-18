#!/usr/bin/python3
"""
Test case for class Square
"""


import unittest
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_default_attr(self):
        """Tests the attributes by default"""
        sq =  Square(62)
        self.assertTrue(sq.width == 62)
        self.assertTrue(sq.height == 62)
        self.assertTrue(sq.x == 0)
        self.assertTrue(sq.y == 0)
        self.assertTrue(sq.id is not None)

    def test_args(self):
        """Tests the args given to rep"""
        sq = Square(2, 4, 5, 6)
        self.assertTrue(sq.width == 2)
        self.assertTrue(sq.height == 2)
        self.assertTrue(sq.x == 4)
        self.assertTrue(sq.y == 5)
        self.assertTrue(sq.id == 6)

    def test_more_args(self):
        """Tests if more arguments passed"""
        with self.assertRaises(TypeError):
            Square(2, 3, 4, 5, 6, 7, 8)

    def test_no_args(self):
        """Tests when no args passed"""
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_square(self):
        """Tests when args are not int"""
        with self.assertRaises(TypeError):
            Square("j")
            Square([5, 4])
            Square({'yes': 1})
        with self.assertRaises(TypeError):
            Square(1, "2")
            Square(1, 2, "3")
            Square(2, 5, "s", 8)

    def test_negative_square(self):
        """Tests when args are negative"""
        with self.assertRaises(ValueError):
            Square(-1)
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, -9, 6, 7)
            Square(1, -2)
            Square(1, 2, -3)
            Square(1, 3, -8, 6)

    def test_class(self):
        """Tests class is indeed Square"""
        self.assertTrue(Square(6), self.__class__ == Square)

    def test_att_values(self):
        """Tests the values given for the
        attributes and error raised where necessary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2", 3, 4, 5)
            Square([2, 3], 4, 5, 6)
            Square({2, })
            Square({"sq": 2})
            Square(None)
            Square((3, 2), 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
            Square(-1)
            Square(0, 2, 3, 4)
            Square(-3, 4, 5, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "g", 3, 4)
            Square(2, [4, 3], 5, 5)
            Square(5, (6, 7), 5, 6)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "yes", 54)
            Square(1, 2, {"k": j}, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2, 3, 4)
            Square(21, -89, 3, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -4, 5)
            Square(56, 98, -100, 99)

    def test_square_area(self):
        """Tests the area of the Square"""
        self.assertEqual(Square(4).area(), 16)
        self.assertEqual(Square(2, 0, 0, 7).area(), 4)
        self.assertEqual(Square(8, 3, 4, 76).area(), 64)
        self.assertEqual(Square(4, 2, 1).area(), 16)

    def test_str(self):
        """Tests how it prints out the Square"""
        sq = Square(1, 2, 3, 44)
        sq.size = 50
        self.assertEqual(str(sq), '[Square] (44) 2/3 - 50')

    def test_to_dictionary(self):
        """Tests the dict representation of square"""
        sq = Square(10, 2, 1, 9)
        sq_dict = sq.to_dictionary()
        sq1 = Square(5)
        sq1.update(**sq_dict)
        self.assertEqual(type(sq_dict), dict)
        self.assertFalse(sq == sq1)
