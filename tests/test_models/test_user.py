#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import unittest
from models.user import User
import pep8


class test_User(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

<<<<<<< HEAD
    def test_pep8_console(self):
        """test pep8 style"""
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['models/user.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')


if __name__ == '__main__':
    unittest.main()
=======
    def test_pep8_User(self):
        """ test pep8 User class"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

    def test_docstring_User(self):
        """ test docstring User class """
        self.assertIsNotNone(User.__doc__)

    def test_attribute_types_User(self):
        """test attributes type of User class"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    @unittest.skipIf(
        getenv('HBNB_TYPE_STORAGE') == 'db',
        "This test only work in Filestorage")
    def test_save_User(self):
        """test save function in class User"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

if __name__ == '__main__':
    unittest.main()

>>>>>>> cd4c93e33e47d8d47247bb74daae22eff0d3b36b
