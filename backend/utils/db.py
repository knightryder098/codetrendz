from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import os
from dotenv import load_dotenv
from flask import current_app

load_dotenv()

def get_db_engine():
    """Create and return a SQLAlchemy engine instance."""
    if current_app and current_app.config.get('TESTING'):
        return create_engine('sqlite:///:memory:', poolclass=QueuePool)
    
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL environment variable is not set")
    
    return create_engine(
        database_url,
        poolclass=QueuePool,
        pool_size=5,
        max_overflow=10,
        pool_timeout=30,
        pool_recycle=1800
    )

def get_db_session():
    """Create and return a SQLAlchemy session."""
    engine = get_db_engine()
    Session = sessionmaker(bind=engine)
    return Session() 