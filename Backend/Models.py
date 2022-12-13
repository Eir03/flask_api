from datetime import timedelta
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True, autoincrement = True, )
    login = Column(String)
    password = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class PostModel(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String)
    content = Column(String)
    creator_id = Column(Integer, ForeignKey('user.id'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}