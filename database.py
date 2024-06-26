import psycopg2


def db_connect(config):
    try:
        connection = psycopg2.connect(
            database=config['database']['dbname'],
            user=config['database']['user'],
            password=config['database']['password'],
            host=config['database']['host'],
            port=config['database']['port']
        )
        return connection, connection.cursor()
    except psycopg2.DatabaseError as e:
        print(f"Database connection error: {e}")
        return None, None


def db_close(connection, cursor):
    if cursor:
        cursor.close()
    if connection:
        connection.close()
