#!/usr/bin/python3
"""Unit tests for FileStorage class"""
import json
import os.path
import unittest

import models

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unit tests suite for FileStorage class"""

    def test_instantiates(self):
        """Tests that FileStorage correctly instantiates"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test __file type is correct after deserialization string-str"""
        file_path_str = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(file_path_str))
    def test_object(self):
        """Test __object is type dict after deserialization object - dict"""
        object_dict = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(object_dict))
    def test_all(self):
        """Test FileStorage: all()"""
        """file is not exit"""
        dict_return = {}
        FileStorage.all(None)
        self.assertTrue(os.path.isfile('file.json'))


if __name__ == "__main__":
    unittest.main()
