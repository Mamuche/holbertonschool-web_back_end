#!/usr/bin/env python3
import unittest
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Tests for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)

        self.assertEqual(str(cm.exception), f"'{expected_key}'")


class TestGetJson(TestCase):
    """Tests for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    # replace the requests.get with mock_get
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests for get_json function"""
        # retrieve test_url and test_payload from parameterized
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        # return the test_playload
        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


# python3 -m unittest -v test_utils.py for the results of each test
