from sqlalchemy import Column, Integer, String, ForeignKey

from src.definitions import Base, MYSQL_VARCHAR_DEFAULT_LENGTH, MYSQL_CASCADE
from src.models import course

TABLE_NAME = 'group_category'
PRIMARY_KEY = 'id'
TABLE_NAME_AND_PRIMARY_KEY = TABLE_NAME+"."+PRIMARY_KEY


class GroupCategory(Base):

    __tablename__ = TABLE_NAME
    id = Column(PRIMARY_KEY, Integer, primary_key=True)
    name = Column(String(MYSQL_VARCHAR_DEFAULT_LENGTH))
    course_id = Column(Integer, ForeignKey(course.TABLE_NAME_AND_PRIMARY_KEY, ondelete=MYSQL_CASCADE))
