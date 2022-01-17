#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
from models.user import User
import pep8


class test_state(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

<<<<<<< HEAD
    def test_pep8_console(self):
        '''test pep8 style'''
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['models/state.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')

    def test_user(self):
        '''Test for State'''
        s = State(name='Of Mind')
        self.assertEqual(str, type(s.name))


if __name__ == '__main__':
=======
        def test_pep8_State(self):
        """ test pep8 Review class"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

    def test_docstring_State(self):
        """test docstring State class"""
        self.assertIsNotNone(State.__doc__)

    def test_attribute_types_State(self):
        """test attributes type of State class"""
        self.assertEqual(type(self.state.name), str)

    @unittest.skipIf(
        getenv('HBNB_TYPE_STORAGE') == 'db',
        "This test only work in Filestorage")
    def test_save_State(self):
        """test save function of State class"""
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

if __name__ == "__main__":
>>>>>>> cd4c93e33e47d8d47247bb74daae22eff0d3b36b
    unittest.main()
