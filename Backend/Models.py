from datetime import timedelta
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String
from sqlalchemy.orm import declarative_base
from flask_jwt_extended import create_access_token
from Backend.Config import token_life_span

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, autoincrement = True, )
    name = Column(String)
    password = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def get_token(self):
        expires_delta = timedelta(minutes=token_life_span)
        token = create_access_token(identity=self.name, expires_delta=expires_delta)
        return token