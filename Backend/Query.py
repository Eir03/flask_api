from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from Backend.Models import UserModel
from Backend.Config import full_url

connection = full_url

engine = create_engine(connection)

session = scoped_session(sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
))
class Query:
    def get_users(self) -> list[UserModel]:
        try:
            data = session.query(UserModel).all()
            return data
        except Exception as ex:
            return ex
    
    def add_user(self, request_data) -> UserModel:
        try:
            user = UserModel(**request_data)
            if session.query(UserModel).filter(UserModel.name == user.name).count() == 0:
                session.add(user)
                session.flush()
                session.commit()
                return user
        except Exception as ex:
            return ex
    
    def get_user(self, request_data) -> UserModel:
        try:
            user = UserModel(**request_data)
            data = session.query(UserModel).filter(
                UserModel.name == user.name and
                UserModel.password == user.password
                ).first()
            return data
        except Exception as ex:
            return ex