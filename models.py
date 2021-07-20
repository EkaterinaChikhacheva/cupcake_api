"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_IMG = 'https://tinyurl.com/demo-cupcake'


def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS GO BELOW!

class Cupcake(db.Model):
    """Department Model"""

    __tablename__ = "cupcakes"
# columns 
    
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    flavor = db.Column(db.String, nullable = False)
    size = db.Column(db.String, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, nullable = False, default = DEFAULT_IMG)

    def __repr__(self):
        return f"<I was too lazy to write stuff here>"

    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }