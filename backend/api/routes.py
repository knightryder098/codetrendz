from flask import Blueprint, jsonify, request, g
from services.github import GitHubService
from models.repository import Repository
from utils.db import get_db_session
from sqlalchemy import desc

api_bp = Blueprint('api', __name__)
github_service = GitHubService()

def get_session():
    """Get the database session from the request context."""
    if hasattr(g, 'session'):
        return g.session
    g.session = get_db_session()
    return g.session

@api_bp.teardown_app_request
def teardown_session(exception=None):
    """Close the database session at the end of the request."""
    session = g.pop('session', None)
    if session is not None:
        session.close()

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'}), 200

@api_bp.route('/repositories', methods=['GET'])
def get_repositories():
    """Get all repositories with optional filtering."""
    session = get_session()
    query = session.query(Repository)
    
    # Apply filters if provided
    language = request.args.get('language')
    if language:
        query = query.filter(Repository.language_stats[language].isnot(None))
    
    # Apply sorting
    sort_by = request.args.get('sort_by', 'stars')
    if sort_by == 'stars':
        query = query.order_by(desc(Repository.stars))
    
    repositories = query.all()
    return jsonify([{
        'id': repo.id,
        'name': repo.name,
        'full_name': repo.full_name,
        'description': repo.description,
        'html_url': repo.html_url,
        'stars': repo.stars,
        'language_stats': repo.language_stats,
        'last_analyzed': repo.last_analyzed.isoformat() if repo.last_analyzed else None
    } for repo in repositories]), 200

@api_bp.route('/repositories/<owner>/<repo>', methods=['GET'])
def get_repository(owner, repo):
    """Get a specific repository by owner and name."""
    session = get_session()
    repository = session.query(Repository).filter_by(full_name=f"{owner}/{repo}").first()
    if not repository:
        return jsonify({'error': 'Repository not found'}), 404
    
    return jsonify({
        'id': repository.id,
        'name': repository.name,
        'full_name': repository.full_name,
        'description': repository.description,
        'html_url': repository.html_url,
        'stars': repository.stars,
        'language_stats': repository.language_stats,
        'last_analyzed': repository.last_analyzed.isoformat() if repository.last_analyzed else None
    }), 200

@api_bp.route('/languages', methods=['GET'])
def get_languages():
    """Get all unique languages from repositories."""
    session = get_session()
    repositories = session.query(Repository).all()
    languages = set()
    for repo in repositories:
        if repo.language_stats:
            languages.update(repo.language_stats.keys())
    return jsonify(list(languages)), 200 