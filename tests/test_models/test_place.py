#!/usr/bin/python3
"""Module for the suite of class Place"""
import unittest
from models.place import Place
import datetime


class TestPlcae(unittest.TestCase):
    """Test for class Place."""

    pl = Place()

    def test_place_attributes(self):
        """Test if place class has the expected attributes."""
        pl = Place()
        self.assertTrue(hasattr(pl, 'city_id'))
        self.assertTrue(hasattr(pl, 'user_id'))
        self.assertTrue(hasattr(pl, 'name'))
        self.assertTrue(hasattr(pl, 'description'))
        self.assertTrue(hasattr(pl, 'number_rooms'))
        self.assertTrue(hasattr(pl, 'number_bathrooms'))
        self.assertTrue(hasattr(pl, 'max_guest'))
        self.assertTrue(hasattr(pl, 'price_by_night'))
        self.assertTrue(hasattr(pl, 'latitude'))
        self.assertTrue(hasattr(pl, 'longitude'))
        self.assertTrue(hasattr(pl, 'amenity_ids'))
        self.assertTrue(hasattr(pl, 'id'))
        self.assertTrue(hasattr(pl, 'created_at'))
        self.assertTrue(hasattr(pl, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.pl.city_id, str)
        self.assertIsInstance(self.pl.user_id, str)
        self.assertIsInstance(self.pl.name, str)
        self.assertIsInstance(self.pl.description, str)
        self.assertIsInstance(self.pl.number_rooms, int)
        self.assertIsInstance(self.pl.number_bathrooms, int)
        self.assertIsInstance(self.pl.max_guest, int)
        self.assertIsInstance(self.pl.price_by_night, int)
        self.assertIsInstance(self.pl.latitude, float)
        self.assertIsInstance(self.pl.longitude, float)
        self.assertIsInstance(self.pl.amenity_ids, list)
        self.assertIsInstance(self.pl.id, str)
        self.assertIsInstance(self.pl.created_at, datetime.datetime)
        self.assertIsInstance(self.pl.updated_at, datetime.datetime)

    def test_place_inheritance(self):
        """Test if User is a inheritance of BaseModel"""
        self.assertIsInstance(self.pl, Place)

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.pl)), "<class 'models.place.Place'>")


if __name__ == '__main__':
    unittest.main()
