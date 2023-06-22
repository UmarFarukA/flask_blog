from sqlalchemy import Column, String, Text, ForeignKey, Integer
from datetime import datetime
from flask_login import UserMixin
from App.extensions import db

class Post(db.Model, UserMixin):
    """A class that defines Post schema"""
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    description = Column(Text, nullable=False)
    post_date = Column(String, nullable=True, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, title, description, user_id):
        self.id = self.id
        self.title = title
        self.description = description
        self.user_id = user_id

    def insert(self):
        """A function that insert a new post"""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """A function that update a given post"""
        db.session.commit()

    def delete(self):
        """A function that deletes a post"""
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Post({self.title}, {self.description}, {self.post_date}, {self.user_id})"