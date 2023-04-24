import datetime
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

from db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    hashed_user_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    problem = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)

    def set_hashed(self, type_):
        self.hashed_user_id = generate_password_hash(type_)

    def check_hashed(self, type_):
        return check_password_hash(self.hashed_user_id, type_)
