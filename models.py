from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    interests = db.Column(db.String(500), nullable=False)
    suggestions = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Submission {self.id}>'
