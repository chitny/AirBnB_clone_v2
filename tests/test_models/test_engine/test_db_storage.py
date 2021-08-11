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

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "can't run if storage is file")
    def test_all_DBStorage(self):
        """Tests for all() method"""
        s = State(name="California")
        storage.new(s)
        storage.save()
        k = '{}.{}'.format(type(s).__name__, s.id)
        dic = storage.all(State)
        self.assertTrue(k in dic.keys())
        s1 = State(name="Arizona")
        storage.new(s1)
        storage.save()
        k1 = '{}.{}'.format(type(s1).__name__, s1.id)
        dic1 = storage.all()
        self.assertTrue(k in dic1.keys())
        self.assertTrue(k1 in dic1.keys())
        u = User(email="derps@herps.com", password="hurrdurr")
        storage.new(u)
        storage.save()
        k2 = '{}.{}'.format(type(u).__name__, u.id)
        dic2 = storage.all(User)
        self.assertTrue(k2 in dic2.keys())
        self.assertFalse(k1 in dic2.keys())
        self.assertFalse(k in dic2.keys())
        self.assertFalse(k2 in dic.keys())

if __name__ == "__main__":
    unittest.main()
