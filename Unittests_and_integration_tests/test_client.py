#!/usr/bin/env python3
"""A github org client"""
import unittest
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

    # patch pour get_json
    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test for public_repos"""

        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        # Ce que get_json doit renvoyer quand il est appelé
        mock_get_json.return_value = test_payload

        # patch pour _public_repos_url
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="https://fake.url/repos"
        ) as mock_repos_url:

            client = GithubOrgClient("google")
            result = client.public_repos()

            # vérification du résultat
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://fake.url/repos")

    # ajout d'un repo, d'une license_key et d'un expected
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test for has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
