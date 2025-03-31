from celery import shared_task
from services.github import GitHubService
from models.repository import Repository
from utils.db import get_db_session
from datetime import datetime

@shared_task
def analyze_repository(owner: str, repo: str):
    """Analyze a GitHub repository and store its data."""
    github_service = GitHubService()
    session = get_db_session()
    
    try:
        # Get repository data
        repo_data = github_service.get_repository(owner, repo)
        languages = github_service.get_repository_languages(owner, repo)
        
        # Create or update repository
        repository = session.query(Repository).filter_by(full_name=f"{owner}/{repo}").first()
        if not repository:
            repository = Repository()
        
        # Update repository data
        repository.name = repo_data['name']
        repository.full_name = repo_data['full_name']
        repository.description = repo_data.get('description')
        repository.html_url = repo_data['html_url']
        repository.stars = repo_data['stargazers_count']
        repository.language_stats = languages
        repository.last_analyzed = datetime.utcnow()
        
        session.add(repository)
        session.commit()
        
        return {
            'status': 'success',
            'repository': repository.full_name
        }
    except Exception as e:
        session.rollback()
        return {
            'status': 'error',
            'error': str(e)
        }
    finally:
        session.close()

@shared_task
def discover_repositories(query: str = 'stars:>1000', limit: int = 100):
    """Discover popular repositories and analyze them."""
    github_service = GitHubService()
    repositories = github_service.search_repositories(query, limit=limit)
    
    for repo in repositories:
        owner, name = repo['full_name'].split('/')
        analyze_repository.delay(owner, name)
    
    return {
        'status': 'success',
        'repositories_discovered': len(repositories)
    } 