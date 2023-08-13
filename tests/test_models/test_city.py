#!/usr/bin/python3
"""Module with unittest suite for class City."""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """Unittest for class City."""
    ct = City()

    def test_city_attributes(self):
        """Test if City class has the expected attributes."""
        ct = City()

        self.assertTrue(hasattr(ct, 'state_id'))
        self.assertTrue(hasattr(ct, 'name'))
        self.assertTrue(hasattr(ct, 'id'))
        self.assertTrue(hasattr(ct, 'created_at'))
        self.assertTrue(hasattr(ct, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.ct.state_id, str)
        self.assertIsInstance(self.ct.name, str)
        self.assertIsInstance(self.ct.id, str)
        self.assertIsInstance(self.ct.created_at, datetime.datetime)
        self.assertIsInstance(self.ct.updated_at, datetime.datetime)

    def test_state_inheritance(self):
        """Test if User is a inheritance of BaseModel"""
        self.assertIsInstance(self.ct, City)

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.ct)), "<class 'models.city.City'>")


if __name__ == '_main__':
    unittest.main()
