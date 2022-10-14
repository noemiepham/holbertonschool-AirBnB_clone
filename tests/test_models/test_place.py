#!/usr/bin/python3
"Unit tests for State class"
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestState(unittest.TestCase):
    """Unit tests for place class"""

    def test_place_isinstance(self):
        """ function that tests an instance """
        somewhere = Place()
        self.assertIsInstance(somewhere, Place)

    def test_place_name(self):
        """ assertequal function"""
        a = Place()
        self.assertEqual("", a.name)
