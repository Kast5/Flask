from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from blog.models.database import db


class Author(db.Model):
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

     user = relationship("User", back_populates="author")


class Author(db.Model):
   ...
   articles = relationship("Article", back_populates="author")


class Author(db.Model):
    ...
    def __str__(self):
        return self.user.username