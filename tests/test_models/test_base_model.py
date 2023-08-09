#!/usr/bin/python3
'''
This module has the unittest for the BaseModel class.
'''
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    '''
    Test cases for the BaseModel class.
    '''
    my_model = BaseModel()

    def test_init(self):
        '''
        Test the __init__ method of BaseModel.
        '''
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
        '''
        Test the _str__ method of BaseModel.
        '''
        my_model = BaseModel()
        m1 = my_model.id
        m2 = my_model.__dict__
        self.assertEqual(str(my_model), "[BaseModel] ({}) {}".format(m1, m2))

    def test_save(self):
        '''
        Test the save method of BaseModel.
        '''
        my_model = BaseModel()
        prev_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(prev_updated_at, my_model.updated_at)

    def test_to_dict(self):
        '''
        Test the to_dict method of BaseModel.
        '''
        my_model = BaseModel()
        m_dict = my_model.to_dict()
        self.assertEqual(m_dict["id"], my_model.id)
        self.assertEqual(m_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(m_dict["updated_at"], my_model.updated_at.isoformat())
        self.assertEqual(m_dict["__class__"], "BaseModel")


if __name__ == '__main__':
    unittest.main
