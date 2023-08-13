#!/usr/bin/python3
'''
This module has the unittest for the BaseModel class.
'''
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import os
import models


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""
    my_model = BaseModel()

    def test_init(self):
        """Test the __init__ method of BaseModel."""
        my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])

    def test_str(self):
        """Test the _str__ method of BaseModel."""
        my_model = BaseModel()
        m1 = my_model.id
        m2 = my_model.__dict__
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(m1, m2))

    def test_save(self):
        """Test the save method of BaseModel."""
        my_model = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(prev_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        my_model = BaseModel()
        m_dict = my_model.to_dict()
        self.assertEqual(m_dict["id"], my_model.id)
        self.assertEqual(m_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(m_dict["updated_at"], my_model.updated_at.isoformat())
        self.assertEqual(m_dict["__class__"], "BaseModel")


class TestBaseModel2(unittest.TestCase):
    """Another test suite for class BaseModel"""
    def setUp(self):
        """Set up a fresh instance of BaseModel for each test."""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up any created files after each test."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """Test the existence of essential attributes in BaseModel"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_id_is_string(self):
        """Test if the id attribute is of string type."""
        self.assertEqual(type(self.model.id), str)

    def test_created_at_is_datetime(self):
        """Test if the created_at is of datetime type"""
        self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_at_is_datetime(self):
        """Test if the updated_at is of datetime type"""
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_save2(self):
        """Test if save method updates the updated_at attribute."""
        first_updated = self.model.updated_at
        self.model.save()
        second_updated = self.model.updated_at
        self.assertNotEqual(first_updated, second_updated)

    def test_to_dict2(self):
        """Test if the to_dict method returns a valid dictionary representation
        """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(
            model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(
            model_dict["updated_at"], self.model.updated_at.isoformat())
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_str2(self):
        """Test if the string representation of BaseModel is as expected"""
        expected_output = "[{}] ({}) {}".format(
            self.model.__class__.__name__, self.model.id, self.model.__dict__)
        model_str = str(self.model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn("'id': '{}'".format(self.model.id), model_str)
        self.assertEqual(expected_output, model_str)

    def test_reload(self):
        """Test if reloading updates the instance correctly."""
        self.model.save()
        model_id = self.model.id

        new_model = BaseModel()
        new_model.id = model_id
        new_model.save()

        models.storage.reload()

        bf = "BaseModel.{}".format(model_id)
        self.assertTrue(bf in models.storage.all())


if __name__ == '__main__':
    unittest.main
