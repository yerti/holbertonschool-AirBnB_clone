#!/usr/bin/python3
"""We will create a test of the BaseModel class"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    """Configure common test environment"""
    def setUp(self):
        self.obj = BaseModel()

    """Tests each attribute"""
    def test_attributes(self):
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    """Tests eachs __str__"""
    def test_str(self):
        obj_str = str(self.obj)
        out_str = "[BaseModel] ({}) {}".format(self.obj.id, self.obj.__dict__)
        self.assertEqual(obj_str, out_str)

    """check if it updates correctly after calling the save method"""
    def test_save(self):
        obj_updated1 = self.obj.updated_at

        self.obj.save()
        obj_updated2 = self.obj.updated_at

        self.assertNotEqual(obj_updated1, obj_updated2)


    """check if the dictionary is created with the attributes"""
    def test_to_dict(self):
        obj_dict = self.obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertNotEqual(obj_dict, self.obj.__dict__)


if __name__ == '__main__':
    unittest.main()
