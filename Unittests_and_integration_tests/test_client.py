#!/usr/bin/env python3
"""A github org client"""
import unittest
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch, PropertyMock

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    # remplace get_json par mock_get_json
    def test_org(self, org_name, mock_get_json):
        """Test for GithubOrgClient"""
        expected_payload = {"name": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, expected_payload)

    def test_public_repos_url(self):
        """Test for _public_repos_url"""
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        # patch pour une propriété de classe (propertyMock)
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = test_payload
            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, test_payload["repos_url"])
