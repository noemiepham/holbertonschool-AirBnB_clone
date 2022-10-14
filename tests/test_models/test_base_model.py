#!/usr/bin/python3
"""Unit tests for BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit tests suite for BaseModel class"""

    def test_save(self):
        """Tests that save method updates the datetime"""
        base = BaseModel()
        old_time = base.updated_at
        base.save()
        self.assertNotEqual(old_time, base.updated_at)

    def test_to_dict(self):
        """
        Tests that to_dict:
            - returns a dictionary
            - that contains all keys/values of __dict__
            - contains __class__ and that this __class__ is the class name
        """
        base = BaseModel()

        """Returns a dictionary"""
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        """Dictionary contains __class__, which is the class name"""
        self.assertTrue("__class__" in base_dict)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(str(base.id), base_dict["id"])
        self.assertIsInstance(base_dict["created_at"], str)
        self.assertIsInstance(base_dict["updated_at"], str)



    def test_str(self):
        """Tests that the string representation has the right format"""
        base = BaseModel()
        right_format = f"[{type(base).__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(str(base), right_format)


if __name__ == "__main__":
    unittest.main()
