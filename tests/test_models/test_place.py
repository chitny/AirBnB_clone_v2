#!/usr/bin/python3
""" Unittest for Amenity """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import place
import pep8
Place = place.Place


class pep8_test(unittest.TestCase):
    """ Test for the place """

    def test_pep8_conformance_place(self):
        """Test that place conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

        def test_pep8_conformance_tplace(self):
            """Test that place conforms to PEP8."""
            pep8s = pep8.StyleGuide(quiet=True)
            result = pep8s.check_files(['tests/test_place.py'])
            self.assertEqual(result.total_errors, 0,
                             "Found code style errors (and warnings).")

        def test_place_module_docstring(self):
            """Test for the place module docstring"""
            self.assertIsNot(__import__("place").__doc__, None,
                             "place.py needs a docstring")
            self.assertTrue(len(__import__("place").__doc__) >= 1,
                            "place.py needs a docstring")

        def test_place_class_docstring(self):
            """Test for the place class docstring"""
            self.assertIsNot(Place.__doc__, None,
                             "place class needs a docstring")
            self.assertTrue(len(Place.__doc__) >= 1,
                            "place class needs a docstring")


class test_Place(test_basemodel):
    """ testing place """

    def __init__(self, *args, **kwargs):
        """  testing place"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ testing place """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """  testing place """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ testing place """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ testing place """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ testing place """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_to_dict_Place(self):
        """Testing place """
        self.assertEqual('to_dict' in dir(self.place), True)

    def test_save_Place(self):
        """ testing place """
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_number_bathrooms(self):
        """ testing place """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ testing place """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ testing place """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ testing place """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ testing place """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ testing place """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

<<<<<<< HEAD
    def test_attribute_types_Review(self):
        """ testing place """
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)
=======
    @unittest.skipIf(
        getenv('HBNB_TYPE_STORAGE') == 'db',
        "This test only work in Filestorage")
    def test_save_Place(self):
        """test if the save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_pep8_Place(self):
        """"  Test pep8 for Place class  """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/place.py'])
        self.assertEqual(p.total_errors, 0, "pep8 errors")

    def test_attribute_types_Place(self):
        """ test for place atributes"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

if __name__ == "__main__":
    unittest.main()
>>>>>>> cd4c93e33e47d8d47247bb74daae22eff0d3b36b
