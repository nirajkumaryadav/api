from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # New field
    author = db.Column(db.String(100), nullable=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'app_name': self.app_name,
            'version': self.version,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'author': self.author  # Include new field in the dictionary
        }