<<<<<<< HEAD
#!/usr/bin/python3
"""test for databasse storage"""
import unittest
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models import storage
import MySQLdb
import pep8


class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "can't run if storage is file")
    def setUp(self):
        """set up for test"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.db = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                      getenv("HBNB_MYSQL_USER"),
                                      getenv("HBNB_MYSQL_PWD"),
                                      getenv("HBNB_MYSQL_DB"))
            self.cursor = self.db.cursor()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "can't run if storage is file")
    def tearDown(self):
        """at the end of the test this will close connection"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.db.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "can't run if storage is file")
    def test_pep8_DBStorage(self):
        """Test for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")


if __name__ == "__main__":
    unittest.main()
=======
#!/usr/bin/python
""" Unittest for DB_Storage """
from models.engine.file_storage import FileStorage
import unittest
import pep8
import os
from models.user import User


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db',
    "This test only work in DBStorage")
class TestDBStorage(unittest.TestCase):
    """ testing """
    @classmethod
    def setUpClass(cls):
        """Tests for User class"""
        cls.user = User()
        cls.user.first_name = "Pichu"
        cls.user.last_name = "Otegui"
        cls.user.email = "correo@hbtn.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """ delete User """
        del cls.user

    def test_pep8_DBStorage(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quiet=True)
        pep = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(pep.total_errors, 0, "pep8 errors")

    def test_all(self):
        """ Testing Object """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """ Testing Object """
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.name = "ElSergio"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

if __name__ == '__main__':
    unittest.main()
>>>>>>> cd4c93e33e47d8d47247bb74daae22eff0d3b36b
