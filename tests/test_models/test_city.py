#!/usr/bin/python3
"""Unit tests for City class"""
import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """Unit tests suite for City class"""

    def test_instance(self):
        """Test instance"""
        hohio = City()
        self.assertIsInstance(hohio, City)

    def test_city_name(self):
        """Test city name"""
        hohio = City()
        self.assertEqual("", hohio.name)

    def test_id(self):
        """Test id"""
        hohio = City()
        self.assertEqual(str, type(hohio.id))

    def test_state_id(self):
        """Test state id"""
        hohio = City()
        self.assertEqual("", hohio.state_id)
