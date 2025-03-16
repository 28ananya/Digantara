# app/__init__.py
from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digantara.db'
    db.init_app(app)
    
    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint)
    
    return app
