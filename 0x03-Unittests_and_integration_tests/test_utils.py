#!/usr/bin/env python3
"""Unittest module for utils, fixtures and client
"""

from parameterized import parameterized
from typing import Dict, List, Tuple, Union
import unittest
from unittest.mock import MagicMock, patch, Mock
from utils import access_nested_map as anm
from utils import get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """Implementation of the utils.get_json unittests
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, py: Union[Dict, bool]) -> None:
        """Test that utils.get_json returns the expected result when passed
        the url
        """
        hi = {'json.return_value': py}
        with patch("requests.get", return_value=Mock(**hi)) as get_req:
            self.assertEqual(get_json(url), py)
            get_req.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Implementation of the utils.memoize unittests
    """

    def test_memoize(self) -> None:
        """test that correct result is returned when calling a_property and
        a_method
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=lambda: 42) as hi:
            test = TestClass()
            self.assertEqual(test.a_property(), 42)
            self.assertEqual(test.a_property(), 42)
            hi.assert_called_once()
