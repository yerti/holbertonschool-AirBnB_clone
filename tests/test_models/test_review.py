#!/usr/bin/python3


import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_attributes(self):
        review = Review()

        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))


if __name__ == '__main__':
    unittest.main()
