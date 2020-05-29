from sqlalchemy import Column, Integer, String

from src.definitions import Base, MYSQL_VARCHAR_DEFAULT_LENGTH

TABLE_NAME = 'course'
PRIMARY_KEY = 'id'
TABLE_NAME_AND_PRIMARY_KEY = TABLE_NAME+"."+PRIMARY_KEY


class Course(Base):

    __tablename__ = TABLE_NAME
    id = Column(PRIMARY_KEY, Integer, primary_key=True)
    canvas_id = Column(Integer)
    name = Column(String(MYSQL_VARCHAR_DEFAULT_LENGTH))
    total_nr_of_students = Column(Integer)
