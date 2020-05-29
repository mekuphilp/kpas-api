from typing import List

from sqlalchemy.orm import sessionmaker

from src.models.course import Course
from src.models.group import Group
from src.models.group_category import GroupCategory


class DatabaseClient:

    def __init__(self, engine):
        Session = sessionmaker(
            bind=engine)
        self.db_session = Session()

    def insert_courses(self, courses: List):
        for course in courses:
            db_course = Course(name=course['name'], total_nr_of_students=course['total_students'])
            self.db_session.add(db_course)
            self.db_session.flush()
            course['db_id'] = db_course.id
        return courses

    def insert_group_categories(self, group_categories: List):
        for group_category in group_categories:
            db_group_category = GroupCategory(name=group_category['name'], course_id=group_category['course_id'])
            self.db_session.add(db_group_category)
            self.db_session.flush()
            group_category['db_id'] = db_group_category.id
        return group_categories

    def insert_groups(self, groups):
        group_dicts = [dict(
            canvas_id=group['id'],
            group_category_id=group['group_category_id'],
            name=group['name'],
            description=group['description'],
            members_count=group['members_count']
        ) for group in groups]
        self.db_session.bulk_insert_mappings(Group, group_dicts)
        self.db_session.flush()

    def truncate_database(self):
        self.db_session.query(Group).delete()
        self.db_session.query(GroupCategory).delete()
        self.db_session.query(Course).delete()

    def commit_session(self):
        self.db_session.commit()
