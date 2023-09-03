import psycopg2


def connect(dsn: str):
    db_conn = psycopg2.connect(dsn)
    cursor = db_conn.cursor()
    return cursor, db_conn
