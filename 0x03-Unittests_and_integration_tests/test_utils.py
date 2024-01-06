#!/usr/bin/python3
"""Unittest module for utils, fixtures and client
"""

from parameterized import parameterized, parameterized_class
from typing import Dict, List, Tuple, Union
import unittest
from utils import access_nested_map as anm


class TestAccessNestedMap(unittest.TestCase):
    """Imnplementation of the utils.access_nested_map uinittests
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            n_map: Dict,
            pa: Tuple[str],
            expected: Union[Dict, int]
            ) -> None:
        """Tests the access_nested_map method from utils"""
        self.assertEqual(anm(n_map, pa), expected)
