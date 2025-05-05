import psycopg2
from initialize.config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # Connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print("\n- - - - - - - -\nConnected to the PostgreSQL server!")
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)