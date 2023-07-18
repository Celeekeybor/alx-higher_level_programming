#!/usr/bin/python3
"""
Test case for class Base
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os
import pep8


class TestPep8(unittest.TestCase):
    """Tests for Pep8 guidelines"""

    def test_pep8(self):
        """Tests pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        files = ["models/base.py", "tests/test_models/test_base.py"]
        results = pep8style.check_files(files)
        self.assertEqual(results.total_errors, 0, "Fix pep8")


class TestBase(unittest.TestCase):
    """Tests for models/base.py"""
    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_id_automatically(self):
        """Tests the assignment of id automatically"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertTrue(b1, self.id == 1)
        self.assertTrue(b2, self.id == 2)
        self.assertTrue(b3, self.id == 3)
        self.assertTrue(b4, self.id == 12)
        self.assertTrue(b5, self.id == 4)

    def test_1_id(self):
        """After run set of ids"""
        Base._Base__nb_objects = 0
        bas = Base()
        self.assertEqual(bas.id, 1)
        t1 = Base(22)
        self.assertEqual(t1.id, 22)
        t2 = Base(-33)
        self.assertEqual(t2.id, -33)
        t3 = Base()
        self.assertEqual(t3.id, 2)

    def test_id_given(self):
        """Tests the matching of id given"""
        self.assertTrue(Base(100), self.id == 100)
        self.assertTrue(Base(-1), self.id == -1)
        self.assertTrue(Base(87432), self.id == 87432)
        self.assertTrue(Base(0), self.id == 0)

    def test_id_is_none(self):
        """Test id will be assigned the increment value
        of private class attribute __nb_objects
        """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_invalid_args(self):
        """Tests more than one args given"""
        with self.assertRaises(TypeError):
            Base(10, 13)

    def test_attribute_error(self):
        """Tests when accessing prvate class attr"""
        b = Base(33)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_private_att_access(self):
        """Tests access of private attribute"""
        with self.assertRaises(AttributeError):
            Base.__nb_objects
            Base.nb_objects
            Base._nb_objects

    def test_class(self):
        """Test whether class is Base"""
        self.assertTrue(Base(2), self.__class__ == Base)

    def test_to_json_string(self):
        """Tests JSON string representation of a dict"""
        dic1 = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        dic2 = {'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10}
        string = Base.to_json_string([dic1, dic2])
        self.assertTrue(type(dic1) == dict)
        self.assertTrue(type(dic2) == dict)
        self.assertTrue(type(string) == str)
        self.assertTrue(string,
                        [{'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
                         {'id': 6, 'width': 7, 'height': 8, 'x': 9, 'y': 10}])

    def test_empty_to_json_string(self):
        """Tests when the dict is empty"""
        dic3 = {}
        stri = Base.to_json_string([dic3])
        self.assertTrue(type(stri) == str)
        self.assertTrue(len(dic3) == 0)
        self.assertTrue(stri, [])

    def test_none_to_json_string(self):
        """Tests when the dict is none"""
        dic4 = None
        stri = Base.to_json_string([dic4])
        self.assertTrue(type(stri) == str)
        self.assertTrue(stri, [])

    def test_save_to_file(self):
        """Tests writing json string rep to file"""
        r1 = Rectangle(10, 7, 2, 8, 9)
        r2 = Rectangle(2, 4, 6, 8, 10)
        sq1 = Square(2, 3, 4, 5)
        sq2 = Square(6, 7, 8, 9)
        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([sq1, sq2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.dumps([r1.to_dictionary(), r2.to_dictionary()]),
                file.read())
        with open("Square.json", "r") as f:
            self.assertEqual(
                json.dumps([sq1.to_dictionary(), sq2.to_dictionary()]),
                f.read())

    def test_empty_save_to_file(self):
        """Tests when the list is empty"""
        Rectangle.save_to_file([])
        Square.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())
        with open("Square.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_none_save_to_file(self):
        """Tests when list is none"""
        Rectangle.save_to_file(None)
        Square.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual('[]', file.read())
        with open("Square.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_one_save_to_file(self):
        """Tests when Square.save_to_file([Square(1)])"""
        sq1 = Square(1)
        sq2 = Square(1, 1)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as file:
            self.assertEqual(
                json.dumps([sq1.to_dictionary(), sq2.to_dictionary()]),
                file.read())

    def test_from_json_string(self):
        """Tests list of json string representation"""
        list1 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        jsonlist1 = Base.from_json_string(list1)
        self.assertTrue(type(list1) == str)
        self.assertTrue(type(jsonlist1) == list)
        self.assertTrue(type(jsonlist1[0]) == dict)
        self.assertTrue(jsonlist1,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
        self.assertTrue(jsonlist1[0],
                        {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_empty_from_json_string(self):
        """Tests when list is empty"""
        list2 = ""
        jsonlist2 = Base.from_json_string(list2)
        self.assertTrue(type(jsonlist2) == list)
        self.assertTrue(jsonlist2 == [])

    def test_none_from_json_string(self):
        """Tests when the list is none"""
        list3 = None
        jsonlist3 = Base.from_json_string(list3)
        self.assertTrue(type(jsonlist3) == list)
        self.assertTrue(jsonlist3 == [])

    def test_create(self):
        """Tests whether create returns an
        instance with all attributes already set
        """
        rec1 = Rectangle(2, 3, 4, 5, 9)
        dic = rec1.to_dictionary()
        rec2 = Rectangle.create(**dic)
        self.assertEqual(str(rec1), '[Rectangle] (9) 4/5 - 2/3')
        self.assertEqual(str(rec2), '[Rectangle] (9) 4/5 - 2/3')
        self.assertIsNot(rec1, rec2)

    def test_load_from_file(self):
        """Tests whether it returns a list of instances"""
        rec1 = Rectangle(5, 7, 2, 4, 9)
        rec2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([rec1, rec2])
        recs = Rectangle.load_from_file()
        self.assertEqual(len(recs), 2)
        for k, v in enumerate(recs):
            if k == 0:
                self.assertEqual(str(v), '[Rectangle] (9) 2/4 - 5/7')
            if k == 1:
                self.assertEqual(str(v), '[Rectangle] (98) 2/2 - 2/4')

    def test_square_save_to_file(self):
        """Tests for square"""
        sq1 = Square(2, 3, 4, 5)
        sq2 = Square(6, 7, 8, 9)
        Square.save_to_file([sq1, sq2])
        sqs = Square.load_from_file()
        self.assertEqual(len(sqs), 2)
        for i, j in enumerate(sqs):
            if i == 0:
                self.assertEqual(str(j), '[Square] (5) 3/4 - 2')
            if i == 1:
                self.assertEqual(str(j), '[Square] (9) 7/8 - 6')

    def test_none_load_from_file(self):
        """Test when fileis none"""
        Rectangle.save_to_file(None)
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_square_load_from_file(self):
        """Tests for square"""
        Square.save_to_file(None)
        sqs = Square.load_from_file()
        self.assertEqual(type(sqs), list)
        self.assertEqual(len(sqs), 0)

    def test_empty_load_from_file(self):
        """Tests load from empty file"""
        Rectangle.save_to_file([])
        recs = Rectangle.load_from_file()
        self.assertEqual(type(recs), list)
        self.assertEqual(len(recs), 0)

    def test_save_load_csv_file(self):
        """Tests serialization and deserialization of csv file"""
        r = Rectangle(2, 3, 4, 5, 6)
        r2 = Rectangle(7, 8, 9, 10, 11)
        rlistinput = [r, r2]
        Rectangle.save_to_file_csv(rlistinput)
        rlistoutput = Rectangle.load_from_file_csv()
        self.assertTrue(rlistinput[0].__str__() == rlistoutput[0].__str__())
        self.assertTrue(rlistinput[1].__str__() == rlistoutput[1].__str__())

    def test_square_csv(self):
        """Test using square"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        slistinput = [s1, s2]
        Square.save_to_file_csv(slistinput)
        slistoutput = Square.load_from_file_csv()
        self.assertTrue(slistinput[0].__str__() == slistoutput[0].__str__())
        self.assertTrue(slistinput[1].__str__() == slistoutput[1].__str__())
