#!/usr/bin/python3
"""Module for the suite of class User"""
import unittest
from models.user import User
from models import storage
import datetime


class TestUser(unittest.TestCase):
    """Test for class User."""

    user = User()

    def test_user_attributes(self):
        """Test if user class has the expected attributes."""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_user_inheritance(self):
        """Test if User is a inheritance of BaseModel"""
        self.assertIsInstance(self.user, User)

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")


if __name__ == '__main__':
    unittest.main()
