import psycopg2
from config import host, user, password, db_name

try:
    # connection to db
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    # the cursor for db operations
    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f'Server version: {cursor.fetchone()}')

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE users(
            id serial PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL);"""
        )

        # connection.commit()
        print(f'[INFO] Table created succesfully!')

    # insert data in db
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO users(first_name, last_name) 
            VALUES
            ('Andrey', 'Dyupin'),
            ('Mihail', 'Masyutin');
            """
        )

        print(f'[INFO] Data was succesfully inserted')

    # get data from db

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT *
            FROM public.users"""
        )
        print(cursor.description)
        print(cursor.fetchall())

    with connection.cursor() as cursor:
        cursor.execute(
            """
            DELETE 
                FROM users
            WHERE first_name = 'Andrey'
            """
        )
        print("[INFO] Data was successfully deleted!")

    with connection.cursor() as cursor:
        cursor.execute(
            """
            DROP TABLE users
            """
        )
        print("[INFO] Table was successfully deleted")
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
