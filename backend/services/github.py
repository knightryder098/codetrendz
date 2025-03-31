import requests
import os
from dotenv import load_dotenv
from typing import Dict, List, Optional

load_dotenv()

class GitHubService:
    BASE_URL = "https://api.github.com"
    
    def __init__(self):
        self.token = os.getenv('GITHUB_API_TOKEN')
        self.headers = {
            'Authorization': f'token {self.token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def get_repository(self, owner: str, repo: str) -> Optional[Dict]:
        """Fetch repository details from GitHub API."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_repository_languages(self, owner: str, repo: str) -> Dict[str, int]:
        """Fetch repository language statistics."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/languages"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def search_repositories(self, query: str, sort: str = 'stars', order: str = 'desc') -> List[Dict]:
        """Search for repositories using GitHub API."""
        url = f"{self.BASE_URL}/search/repositories"
        params = {
            'q': query,
            'sort': sort,
            'order': order
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()['items'] 