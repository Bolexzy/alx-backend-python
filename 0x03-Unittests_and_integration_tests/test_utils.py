#!/usr/bin/env python3
''' Unittest module for utils.access_nested_map
'''

import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
import requests
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    ''' Class for testing Nested Map function
    '''

    @parameterized.expand([
          ({"a": 1}, ["a",], 1),
          ({"a": {"b": 2}}, ["a",], {"b": 2}),
          ({"a": {"b": 2}}, ["a", "b"], 2)
      ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        ''' Test method returns correct output
        '''
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand([
        ({}, ["a",], 'a'),
        ({"a": 1}, ["a", "b"], 'b')
        ])
    def test_access_nested_map_exception(self, nested_map, path, key_error):
        ''' Test method raises correct exception
        '''
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(key_error, e.exception)


class TestGetJson(unittest.TestCase):
    ''' Class for testing get_json function
    '''

    @parameterized.expand([
          ("http://example.com", {"payload": True}),
          ("http://holberton.io", {"payload": False})
      ])
    def test_get_json(self, test_url, test_payload):
        ''' Test method returns correct output, test_payload.
        '''
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('requests.get', return_value=mock_response):
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            # check that mocked method called once per input
            mock_response.json.assert_called_once()
