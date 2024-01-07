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

    @patch("client.get_json")
    def test_public_repos(self, m_mock: MagicMock) -> None:
        """ Implementation of the public repos unittests
        """
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                        "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                    },
                    "html_url": "https://github.com/google/episodes.dart",
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "pushed_at": "2014-10-09T21:39:33Z",
                    "git_url": "git://github.com/google/episodes.dart.git",
                    "ssh_url": "git@github.com:google/episodes.dart.git",
                    "clone_url": "https://github.com/google/episodes.dart.git",
                    "svn_url": "https://github.com/google/episodes.dart",
                    "homepage": None,
                    "size": 191,
                    "stargazers_count": 12,
                    "watchers_count": 12,
                    "language": "Dart",
                    "has_issues": True,
                    "has_projects": True,
                    "has_downloads": True,
                    "has_wiki": True,
                    "has_pages": False,
                    "forks_count": 22,
                    "mirror_url": None,
                    "archived": False,
                    "disabled": False,
                    "open_issues_count": 0,
                    "forks": 22,
                    "open_issues": 0,
                    "watchers": 12,
                    "default_branch": "master",
                    "permissions": {
                        "admin": False,
                        "push": False,
                        "pull": True
                    }
                },
                {
                    "id": 8165161,
                    "node_id": "MDEwOlJlcG9zaXRvcnk4MTY1MTYx",
                    "name": "ios-webkit-debug-proxy",
                    "full_name": "google/ios-webkit-debug-proxy",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": ('https://api.github.com/repos/google/'
                            'ios-webkit-debug-proxy'),
                    "created_at": "2013-02-12T19:08:19Z",
                    "updated_at": "2019-12-04T02:06:43Z",
                    "pushed_at": "2019-11-24T07:02:13Z",
                    "homepage": "",
                    "size": 680,
                    "stargazers_count": 4630,
                    "watchers_count": 4630,
                    "language": "C",
                    "has_issues": True,
                    "has_projects": True,
                    "has_downloads": True,
                    "has_wiki": False,
                    "has_pages": False,
                    "forks_count": 395,
                    "mirror_url": None,
                    "archived": False,
                    "disabled": False,
                    "open_issues_count": 24,
                }
            ]
        }
        m_mock.return_value = test_payload['repos']
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mocked:
            mocked.return_value = test_payload['repos']
            self.assertEqual(GOC("google").public_repos(),
                             [
                                 "episodes.dart",
                                 "ios-webkit-debug-proxy"
                             ])
            mocked.assert_called_once()
        m_mock.assert_called_once()
