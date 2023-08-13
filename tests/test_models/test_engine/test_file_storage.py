#!/usr/bin/python3
"""Module for the unittes suite of class FileStorage"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """Setup up the testing environment."""
        cls.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test the all method."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test the new method."""
        model = BaseModel()
        self.storage.new(model)
        self.assertTrue("BaseModel.{}".format(model.id) in self.storage.all())

    def test_save_reload(self):
        """Test the save and reload methods."""
        model = BaseModel()
        self.storage.new(model)

        new_storage = FileStorage()
        new_storage.reload()

        loaded_objects = new_storage.all()
        self.assertTrue("BaseModel.{}".format(model.id) in loaded_objects)
        loaded_model = loaded_objects["BaseModel.{}".format(model.id)]
        self.assertEqual(loaded_model.id, model.id)
        self.assertEqual(loaded_model.created_at, model.created_at)

    def test_reload(self):
        """Test reloading with an unrecognized class name."""
        data = {
            "BaseModel.1234": {
                "__class__": "BaseModel",
                "id": "1234"
            }
        }
        with open(FileStorage._FileStorage__file_path, 'w') as file:
            json.dump(data, file)

        self.storage.reload()

        loaded_objects = self.storage.all()
        self.assertTrue("BaseModel.1234" in loaded_objects)
        loaded_model = loaded_objects["BaseModel.1234"]
        self.assertIsInstance(loaded_model, BaseModel)
        self.assertEqual(loaded_model.id, "1234")


if __name__ == '__main__':
    unittest.main()
