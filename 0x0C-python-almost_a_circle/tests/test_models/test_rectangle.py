#!/usr/bin/python3
"""Module for test Rectangle class"""
import unittest
import unittest.mock
import io
import random
from models import rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class"""

    def test_doc_module(self):
        """Module has documentation"""
        doc = rectangle.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_class(self):
        """Class has documentation"""
        doc = rectangle.Rectangle.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_constructor(self):
        """Constructor has documentation"""
        doc = rectangle.Rectangle.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_extra_arguments(self):
        """Pass extra arguments"""
        with self.assertRaises(TypeError):
            rectangle.Rectangle(12, 12, 0, 0, 0, 123)

    def test_missing_arguments(self):
        """Missing arguments in constructor"""

        # Missing one argument
        with self.subTest():
            with self.assertRaises(TypeError):
                rectangle.Rectangle(12)

        # Missing all the arguments
        with self.subTest():
            with self.assertRaises(TypeError):
                rectangle.Rectangle()

    def test_area(self):
        """Calculates the area of a rectangle"""
        rec = rectangle.Rectangle(3, 2)
        self.assertIs(rec.area(), 6)

        rec.width = 2
        rec.height = 10
        self.assertIs(rec.area(), 20)

        rec.width = 8
        rec.height = 7
        self.assertIs(rec.area(), 56)

        rec.width = 3
        rec.height = 1
        self.assertIs(rec.area(), 3)

    def test_area_with_argument(self):
        """Area method with an argument"""
        rect = rectangle.Rectangle(12, 2)

        with self.assertRaises(TypeError):
            rect.area(12)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout_display(self, rect, expected_output, mock_stdout):
        """Compare the stdout with an expected output"""
        rect.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        """Normal pattern printed"""
        rect = rectangle.Rectangle(4, 6)
        output = '''####
####
####
####
####
####
'''
        self.assert_stdout_display(rect, output)

        rect = rectangle.Rectangle(2, 3, 2, 2)
        output = '''

  ##
  ##
  ##
'''
        self.assert_stdout_display(rect, output)

        rect = rectangle.Rectangle(3, 2, 1, 0)
        output = ''' ###
 ###
'''
        self.assert_stdout_display(rect, output)

    def test_display_with_argument(self):
        """Pass an extra argument to display method"""
        rect = rectangle.Rectangle(13, 2)

        with self.assertRaises(TypeError):
            rect.display(12)

    def test_str_object(self):
        """Verify the output of str"""
        rect = rectangle.Rectangle(12, 2)
        str_out = rect.__str__()
        str_expected = '[Rectangle] (14) 0/0 - 12/2'
        self.assertEqual(str_out, str_expected)

        rect2 = rectangle.Rectangle(4, 6, 2, 1, 12)
        str_out = rect2.__str__()
        str_expected = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(str_out, str_expected)

        rectangle.Rectangle(4, 6, 2, 1)
        rect3 = rectangle.Rectangle(4, 6, 2, 1)
        str_out = rect3.__str__()
        str_expected = '[Rectangle] (16) 2/1 - 4/6'
        self.assertEqual(str_out, str_expected)

    def test_str_with_arguments(self):
        """Pass an extra argument to str method"""
        rect = rectangle.Rectangle(12, 12)

        with self.assertRaises(TypeError):
            rect.__str__(12)

    @staticmethod
    def list2str(*my_list):
        """Convert a list into a string"""
        literal = ''
        for x in my_list:
            literal += str(x) + ', '

        return literal.rstrip(', ')

    @staticmethod
    def get_value(elements, idx):
        """Get the value of a tuple or default value"""
        if len(elements) <= idx:
            return 10

        return elements[idx]

    @staticmethod
    def get_expected(*args):
        """Generates the expected output for method update"""
        id_rect = args[0]
        w = TestRectangle.get_value(args, 1)
        h = TestRectangle.get_value(args, 2)

        x = TestRectangle.get_value(args, 3)
        y = TestRectangle.get_value(args, 4)

        literal = '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(id_rect, x, y, w, h)

        return literal

    def test_update_args(self):
        """Update all the possible positions of the rectangle with *args"""
        arguments = [89, 2, 3, 4, 5, 7, 8]
        rect = rectangle.Rectangle(10, 10, 10, 10)
        self.assertEqual(rect.__str__(), '[Rectangle] (18) 10/10 - 10/10')

        for i in range(5):
            l2str = TestRectangle.list2str(*arguments[:i + 1])
            expression = 'rect.update({})'.format(l2str)
            eval(expression)
            expected_out = self.get_expected(*arguments[:i + 1])
            with self.subTest(i=i):
                self.assertEqual(rect.__str__(), expected_out)

    def test_update_kwargs(self):
        """Update all the possible positions of the rectangle with kwargs"""
        rect = rectangle.Rectangle(10, 10, 10, 10)
        self.assertEqual(rect.__str__(), '[Rectangle] (19) 10/10 - 10/10')

        rect.update(height=1)
        self.assertEqual(rect.__str__(), '[Rectangle] (19) 10/10 - 10/1')

        rect.update(width=1, x=2)
        self.assertEqual(rect.__str__(), '[Rectangle] (19) 2/10 - 1/1')

        rect.update(y=1, width=2, x=3, id=89)
        self.assertEqual(rect.__str__(), '[Rectangle] (89) 3/1 - 2/1')

        rect.update(x=1, height=2, y=3, width=4)
        self.assertEqual(rect.__str__(), '[Rectangle] (89) 1/3 - 4/2')

        rect.update(120, 123, x=12, y=32)
        self.assertEqual(rect.__str__(), '[Rectangle] (120) 1/3 - 123/2')

    def test_dictionary(self):
        """Dictionary representation of a rectangle"""
        rect = rectangle.Rectangle(13, 14, 15, 16, 12)
        expected = {'id': 12, 'width': 13, 'height': 14, 'x': 15, 'y': 16}
        self.assertEqual(rect.to_dictionary(), expected)

        with self.assertRaises(TypeError):
            rect.to_dictionary(12)


if __name__ == '__main__':
    unittest.main()
