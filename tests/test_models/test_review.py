#!/usr/bin/python3
"Unit tests for State class"
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestState(unittest.TestCase):
    """Unit tests for review class"""

    def test_review_text(self):
        """ assertequal function"""
        b = Review()
        self.assertEqual("", b.text)
