#!/usr/bin/python3
"""Module for test Square class"""
import unittest
from models import square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Tests for square class"""

    def test_doc_module(self):
        """Module has documentation"""
        doc = square.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_class(self):
        """Class has documentation"""
        doc = square.Square.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_constructor(self):
        """Constructor has documentation"""
        doc = square.Square.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_extra_argument(self):
        """Pass extra argument into constructor"""
        with self.assertRaises(TypeError):
            square.Square(12, 12, 12, 12, 12)

    def test_constructor(self):
        """Creating multiple objects"""
        Base._Base__nb_objects = 0
        sq = square.Square(12, 2, 0)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, 1)
        self.assertEqual(sq.width, 12)
        self.assertEqual(sq.width, sq.height)

    def test_str_object(self):
        """Compare the __str__ method"""
        sq = square.Square(12, 2, 30, 25)
        self.assertEqual(sq.__str__(), '[Square] (25) 2/30 - 12')

    def test_size(self):
        """Using getter and setter of size"""
        sq = square.Square(12, 2, 30, 25)

        sq.size = 12
        self.assertEqual(sq.size, 12)

    def test_size_error(self):
        """Using size methods wrong"""
        sq = square.Square(12, 2, 30, 25)

        with self.assertRaises(TypeError):
            sq.size = "12"

        with self.assertRaises(ValueError):
            sq.size = -12

    def test_update(self):
        """Update a square from *args"""
        pass

    def test_dictionary(self):
        """Dictionary representation of a square"""
        rect = square.Square(13, 15, 16, 12)
        expected = {'id': 12, 'size': 13, 'x': 15, 'y': 16}
        self.assertEqual(rect.to_dictionary(), expected)

        with self.assertRaises(TypeError):
            rect.to_dictionary(12)


if __name__ == '__main__':
    unittest.main()
