#!/usr/bin/env python3
"""Client unittests implementation
"""

from parameterized import parameterized
from typing import Dict, List, Tuple, Union
import unittest
from unittest.mock import MagicMock, patch, Mock, PropertyMock
from client import GithubOrgClient as GOC


class TestGithubOrgClient(unittest.TestCase):
    """Implementation of the client.GithubOrgClient unittests
    """

    @parameterized.expand([
        ("google", {'login': 'google'}),
        ("abc", {'login': 'abc'})
    ])
    @patch("client.get_json")
    def test_org(self, org: str, body: Dict, m_mock: MagicMock) -> None:
        """Implementation of the org unittests
        """
        m_mock.return_value = MagicMock(return_value=body)
        temp = GOC(org)
        self.assertEqual(temp.org(), body)
        m_mock.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """Implementation of the public repos url unittests
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mocked:
            mocked.return_value = {
                'repos_url': "https://api.github.com/users/google/repos"
            }
            self.assertEqual(GOC("google")._public_repos_url,
                             "https://api.github.com/users/google/repos")
