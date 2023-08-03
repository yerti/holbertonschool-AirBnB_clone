#!/usr/bin/python3
"""We will create a test of the BaseModel class"""


import datetime
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    """Configure common test environment"""
    def setUp(self):
        obj = BaseModel()

    """Tests each attribute"""
    def test_attributes(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    """Tests eachs __str__"""
    def test_str(self):
        obj = BaseModel()
        obj_str = str(obj)
        out_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(obj_str, out_str)

    """check if it updates correctly after calling the save method"""
    def test_save(self):
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(prev_updated_at, obj.updated_at)

    """check if the dictionary is created with the attributes"""
    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertNotEqual(obj_dict, obj.__dict__)


if __name__ == '__main__':
    unittest.main()
