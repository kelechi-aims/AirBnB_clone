#!/usr/bin/python3
"""Module for the suite of class Amenity"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Test for class Amenity."""

    am = Amenity()

    def test_amenity_attributes(self):
        """Test if user class has the expected attributes."""
        am = Amenity()
        self.assertTrue(hasattr(am, 'name'))
        self.assertTrue(hasattr(am, 'id'))
        self.assertTrue(hasattr(am, 'created_at'))
        self.assertTrue(hasattr(am, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.am.name, str)
        self.assertIsInstance(self.am.id, str)
        self.assertIsInstance(self.am.created_at, datetime.datetime)
        self.assertIsInstance(self.am.updated_at, datetime.datetime)

    def test_amenity_inheritance(self):
        """Test if User is a inheritance of BaseModel"""
        self.assertIsInstance(self.am, Amenity)

    def test_class_exists(self):
        """tests if class exists"""
        cc = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.am)), cc)


if __name__ == '__main__':
    unittest.main()
