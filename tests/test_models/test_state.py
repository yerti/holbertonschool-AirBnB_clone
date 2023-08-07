#!/usr/bin/python3


import unittest
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))


if __name__ == '__main__':
    unittest.main()
