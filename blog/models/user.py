from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"

email = Column(String(255), nullable=False, default="", server_default="")

from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from blog.security import flask_bcrypt

class User(db.Model, UserMixin):
    ...

    _password = Column(LargeBinary, nullable=True)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)


class User(db.Model, UserMixin):
    ...
    first_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False, nullable=False, default="", server_default="")


class User(db.Model, UserMixin):
    ...
    email = Column(String(255), unique=True, nullable=False, default="", server_default="")


from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    ...

    author = relationship("Author", uselist=False, back_populates="user")


