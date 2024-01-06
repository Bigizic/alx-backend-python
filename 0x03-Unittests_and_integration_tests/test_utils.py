#!/usr/bin/python3
"""Unittest module for utils, fixtures and client
"""

from parameterized import parameterized, parameterized_class
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Imnplementation of the utils.access_nested_map uinittests
    """

    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, n_map, pa):
        """Tests the access_nested_map method from utils"""
        self.assertEqual(access_nested_map(n_map, pa), n_map[pa[0]]
                         if len(pa) < 2 else n_map[pa[0]][pa[1]])
