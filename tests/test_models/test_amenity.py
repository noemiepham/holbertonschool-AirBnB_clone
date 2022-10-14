#!/usr/bin/python3
""" Unit test for Amenity """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    "Unit tests suite for Amenity class"

    def test_class(self):
        testamenity = Amenity()
        self.assertEqual(testamenity.__class__.__name__, "Amenity")

    def test_attributes_Class(self):
        """Test attributes Class """
        my_amenity = Amenity()
        my_amenity.name = "Hello-Holberton"
        self.assertEqual(my_amenity.name, 'Hello-Holberton')

    def test_subclass(self):
        testamenity = Amenity()
        self.assertTrue(issubclass(testamenity.__class__, BaseModel))

    def test_Amenity_name(self):
        """ assertequal function"""
        a = Amenity()
        self.assertEqual("", a.name)
