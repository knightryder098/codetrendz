from flask import Flask
from flask_cors import CORS
from celery import Celery
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configure app
    app.config.update(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev'),
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        CELERY_BROKER_URL=os.getenv('REDIS_URL'),
        CELERY_RESULT_BACKEND=os.getenv('REDIS_URL')
    )

    # Initialize Celery
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND']
    )
    celery.conf.update(app.config)

    # Register blueprints
    from api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app, celery

# Create the application instance
app, celery = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 