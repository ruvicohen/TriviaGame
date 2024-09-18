import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQL_URI


def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)

def create_users_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(50) NOT NULL
        )
        ''')
        connection.commit()

def create_questions_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY,
            question_text VARCHAR(255) NOT NULL,
            correct_answer VARCHAR(255) NOT NULL
        )
        ''')
        connection.commit()

def create_answers_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS answers (
            id SERIAL PRIMARY KEY,
            question_id INT NOT NULL,
            incorrect_answer VARCHAR(255) NOT NULL,
            FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
        )
        ''')
        connection.commit()

def create_user_answers_table():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_answers (
            id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            question_id INT NOT NULL,
            is_correct BOOLEAN NOT NULL,
            time_taken INTERVAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
        )
        ''')
        connection.commit()

def create_tables():
    create_users_table()
    create_questions_table()
    create_answers_table()
    create_user_answers_table()


def drop_all_tables():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS user_answers;
        DROP TABLE IF EXISTS answers;
        DROP TABLE IF EXISTS questions;
        DROP TABLE IF EXISTS users;
    ''')

    connection.commit()
    cursor.close()
    connection.close()

