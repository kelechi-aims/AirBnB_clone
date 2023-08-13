#!/usr/bin/python3
"""Module with unittest suite for class State."""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """Unittest for class State."""
    st = State()

    def test_state_attributes(self):
        """Test if State class has the expected attributes."""
        st = State()

        self.assertTrue(hasattr(st, 'name'))
        self.assertTrue(hasattr(st, 'id'))
        self.assertTrue(hasattr(st, 'created_at'))
        self.assertTrue(hasattr(st, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.st.name, str)
        self.assertIsInstance(self.st.id, str)
        self.assertIsInstance(self.st.created_at, datetime.datetime)
        self.assertIsInstance(self.st.updated_at, datetime.datetime)

    def test_state_inheritance(self):
        """Test if User is a inheritance of BaseModel"""
        self.assertIsInstance(self.st, State)

    def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.st)), "<class 'models.state.State'>")


if __name__ == '_main__':
    unittest.main()
