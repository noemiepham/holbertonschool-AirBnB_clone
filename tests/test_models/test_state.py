#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Unit tests suite for State class"""

    def test_instance(self):
        """Test instance"""
        hello = State()
        self.assertIsInstance(hello, State)

    def test_state_name(self):
        """Test state name"""
        hello = State()
        self.assertEqual("", hello.name)

    def test_id(self):
        """Test id"""
        hello = State()
        self.assertEqual(str, type(hello.id))
