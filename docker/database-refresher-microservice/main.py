from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from src.api_client import ApiClient
from src.db_client import DatabaseClient
from src.definitions import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, Base, DB_DATABASE, MYSQL_ROOT_PASSWORD
import logging
import sys


def refresh_database():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logger = logging.getLogger()

    db_root_url = f"mysql+mysqlconnector://root:{MYSQL_ROOT_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    db_url = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

    if not database_exists(db_root_url):
        create_database(db_root_url)

    root_engine = create_engine(db_root_url)
    with root_engine.connect() as conn:
        conn.execute(f"GRANT CREATE, SELECT, INSERT, DELETE ON {DB_DATABASE}.* TO '{DB_USERNAME}';")

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    api_client = ApiClient()
    db_client = DatabaseClient(engine)
    db_client.truncate_database()
    logger.info("Truncated database")

    courses = api_client.get_courses()
    courses = db_client.insert_courses(courses)
    logger.info(f"Inserted {len(courses)} courses")

    all_group_categories = []

    for course in courses:
        group_categories_for_course = api_client.get_group_categories_by_course(course['id'])
        for group_category in group_categories_for_course:
            group_category['course_id'] = course['db_id']

        all_group_categories += group_categories_for_course

    all_group_categories = db_client.insert_group_categories(all_group_categories)
    logger.info(f"Inserted {len(all_group_categories)} group categories")

    all_groups = []

    for group_category in all_group_categories:
        groups_for_course = api_client.get_groups_by_group_category_id(group_category['id'])
        for group in groups_for_course:
            group['group_category_id'] = group_category['db_id']

        all_groups += groups_for_course

    db_client.insert_groups(all_groups)
    logger.info(f"Inserted {len(all_groups)} groups")

    db_client.commit_session()
