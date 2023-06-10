from sqlalchemy import Column, String, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()

login_manager = LoginManager()
# migrate = Migrate()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """Defines a User model"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    image_path = Column(String(120), nullable=True, default='default.png')
    created_at = Column(String, nullable=True, default=datetime.utcnow)
    posts = relationship('Post', backref="author", lazy=True)

    def __init__(self, username, email, password):
        self.id = self.id
        self.username = username
        self.email = email
        self.password = password

    def insert(self):
        """Insert a new user"""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """A function that updates the user"""
        db.session.commit()

    def delete(self):
        """A function that deletes a user"""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.created_at})"