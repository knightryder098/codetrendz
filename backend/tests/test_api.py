import pytest
from core.app import create_app
from models.repository import Repository
from models.base import Base
from utils.db import get_db_session, get_db_engine
from datetime import datetime
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import g

@pytest.fixture
def app():
    app, _ = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def db_session(app):
    with app.app_context():
        engine = get_db_engine()
        connection = engine.connect()
        transaction = connection.begin()
        
        # Create all tables
        Base.metadata.create_all(connection)
        
        # Create a session factory bound to this connection
        session_factory = sessionmaker(bind=connection)
        session = scoped_session(session_factory)
        
        # Set the session in the Flask application context
        g.session = session
        
        yield session
        
        # Clean up
        g.pop('session', None)
        session.remove()
        transaction.rollback()
        connection.close()

def test_health_check(client):
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_get_repositories_empty(client, db_session):
    response = client.get('/api/v1/repositories')
    assert response.status_code == 200
    assert response.json == []

def test_get_repository_not_found(client, db_session):
    response = client.get('/api/v1/repositories/owner/repo')
    assert response.status_code == 404
    assert 'error' in response.json

def test_get_languages_empty(client, db_session):
    response = client.get('/api/v1/languages')
    assert response.status_code == 200
    assert response.json == [] 