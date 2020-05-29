import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from src.definitions import Base, MYSQL_VARCHAR_DEFAULT_LENGTH, MYSQL_CASCADE
from src.models import group_category

TABLE_NAME = 'group'
PRIMARY_KEY = 'id'
TABLE_NAME_AND_PRIMARY_KEY = TABLE_NAME+"."+PRIMARY_KEY


class Group(Base):

    __tablename__ = TABLE_NAME
    id = Column(PRIMARY_KEY, Integer, primary_key=True)
    canvas_id = Column(Integer)
    group_category_id = Column(Integer, ForeignKey(group_category.TABLE_NAME_AND_PRIMARY_KEY, ondelete=MYSQL_CASCADE))
    name = Column(String(MYSQL_VARCHAR_DEFAULT_LENGTH))
    description = Column(String(MYSQL_VARCHAR_DEFAULT_LENGTH))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    members_count = Column(Integer)
