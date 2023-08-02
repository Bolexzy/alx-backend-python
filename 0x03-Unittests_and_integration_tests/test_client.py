#!/usr/bin/env python3
''' Unittest module to test client.py
'''

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    ''' Class for testing GithubOrgClient
    '''

    @parameterized.expand([
            ('google'),
            ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, org, mock_json):
        ''' Test that GithubOrgClient.org returns the correct value
        '''
        client = GithubOrgClient(org)
        result = client.org

        url = f'https://api.github.com/orgs/{org}'

        # Check that get_json was called once with the expected argument
        mock_json.assert_called_once_with(url)
        self.assertEqual(result, mock_json.return_value)
