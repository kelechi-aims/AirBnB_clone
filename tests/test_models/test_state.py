#!/usr/bin/python3
"""Module with unittest suite for class State."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unittest for class State."""
    def test_state_attributes(self):
        """Test if State class has the expected attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))


if __name__ == '_main__':
    unittest.main()
