import os
from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__)

    # Store SQLite file in the app directory instead of /data
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    db_path = os.getenv('DATABASE_URL', f'sqlite:///{os.path.join(BASE_DIR, "digantara.db")}')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
