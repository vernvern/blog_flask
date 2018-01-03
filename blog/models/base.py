from blog import db

from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declared_attr


class BaseModel(object):
    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()
    id = db.Column(db.Integer, primary_key=True)
    date_create = db.Column(TIMESTAMP, server_default=func.now())
    date_modify = db.Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())
