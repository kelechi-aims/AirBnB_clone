#!/usr/bin/python3
"""Module for the suite of class Review"""
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """Test for class Review."""

    re = Review()

    def test_review_attributes(self):
        """Test if review class has the expected attributes."""
        re = Review()
        self.assertTrue(hasattr(re, 'place_id'))
        self.assertTrue(hasattr(re, 'user_id'))
        self.assertTrue(hasattr(re, 'text'))
        self.assertTrue(hasattr(re, 'id'))
        self.assertTrue(hasattr(re, 'created_at'))
        self.assertTrue(hasattr(re, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.re.place_id, str)
        self.assertIsInstance(self.re.user_id, str)
        self.assertIsInstance(self.re.text, str)
        self.assertIsInstance(self.re.id, str)
        self.assertIsInstance(self.re.created_at, datetime.datetime)
        self.assertIsInstance(self.re.updated_at, datetime.datetime)

    def test_review_inheritance(self):
        """Test if User is a inheritance of BaseModel"""
        self.assertIsInstance(self.re, Review)

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.re)), "<class 'models.review.Review'>")


if __name__ == '__main__':
    unittest.main()
