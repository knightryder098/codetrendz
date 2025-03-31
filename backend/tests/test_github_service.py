import pytest
from services.github import GitHubService
from unittest.mock import patch, MagicMock

@pytest.fixture
def github_service():
    return GitHubService()

def test_get_repository(github_service):
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'name': 'test-repo',
            'full_name': 'owner/test-repo',
            'description': 'Test repository',
            'html_url': 'https://github.com/owner/test-repo',
            'stargazers_count': 1000
        }
        mock_get.return_value = mock_response

        result = github_service.get_repository('owner', 'test-repo')
        assert result['name'] == 'test-repo'
        assert result['full_name'] == 'owner/test-repo'
        assert result['stargazers_count'] == 1000

def test_get_repository_languages(github_service):
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'Python': 1000,
            'JavaScript': 500
        }
        mock_get.return_value = mock_response

        result = github_service.get_repository_languages('owner', 'test-repo')
        assert result['Python'] == 1000
        assert result['JavaScript'] == 500

def test_search_repositories(github_service):
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'items': [
                {
                    'name': 'repo1',
                    'full_name': 'owner1/repo1',
                    'description': 'First repo'
                },
                {
                    'name': 'repo2',
                    'full_name': 'owner2/repo2',
                    'description': 'Second repo'
                }
            ]
        }
        mock_get.return_value = mock_response

        result = github_service.search_repositories('stars:>1000')
        assert len(result) == 2
        assert result[0]['name'] == 'repo1'
        assert result[1]['name'] == 'repo2' 