from blog import db

import flask_sqlalchemy
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class BaseModel(flask_sqlalchemy.Model):
    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()
    id = db.Column(db.Integer, primary_key=True)
    date_create = db.Column(TIMESTAMP, server_default=func.now())
    date_modify = db.Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())
