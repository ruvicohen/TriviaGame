# import pytest
#
# from Repository.database import create_tables, get_db_connection, drop_all_tables
# from Repository.seed import seed
# from Repository.trivia_repository import load_trivia_data_from_api
#
#
# @pytest.fixture(scope="module")
# def setup_database():
#     create_tables()
#     load_trivia_data_from_api()
#     yield
#     drop_all_tables()
#
#
# def test_create_tables(setup_database):
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute("""
#         SELECT EXISTS (
#             SELECT FROM information_schema.tables
#             WHERE table_name IN ('users', 'questions', 'answers', 'user_answers')
#         );
#     """)
#     tables_exist = all([row[0] for row in cur.fetchall()])
#     assert tables_exist
#
#
# def test_drop_all_tables():
#     drop_all_tables()
#
#     conn = get_db_connection()
#     cur = conn.cursor()
#
#     cur.execute("""
#         SELECT EXISTS (
#             SELECT FROM information_schema.tables
#             WHERE table_name IN ('users', 'questions', 'answers', 'user_answers')
#         );
#     """)
#     tables_exist = any([row[0] for row in cur.fetchall()])
#
#     assert not tables_exist
#
#     cur.close()
#     conn.close()
