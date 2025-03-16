# app/models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class APILog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    algorithm_name = db.Column(db.String(50))
    input_data = db.Column(db.String)
    output_data = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
