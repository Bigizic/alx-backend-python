#!/usr/bin/env python3
"""Unittest module for utils, fixtures and client
"""

from parameterized import parameterized
from typing import Dict, List, Tuple, Union
import unittest
from utils import access_nested_map as anm


class TestAccessNestedMap(unittest.TestCase):
    """Imnplementation of the utils.access_nested_map unittests
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, n_map: Dict, pa: Tuple[str],
                               expect: Union[Dict, int]) -> None:
        """Tests the access_nested_map method from utils"""
        self.assertEqual(anm(n_map, pa), expect)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, n_map: Dict,
                                         pa: Tuple[str]) -> None:
        """Handles utils.access_nested_map exceptions"""
        with self.assertRaises(KeyError):
            anm(n_map, pa)
