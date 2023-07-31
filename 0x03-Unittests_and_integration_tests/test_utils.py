#!/usr/bin/env python3
''' Unittest module for utils.access_nested_map
'''

import unittest
from utils import access_nested_map
from parameterized import parameterized


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
