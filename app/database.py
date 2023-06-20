# import time
# import psycopg
# from psycopg.rows import dict_row
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         # Connect to an existing database using psycopg -- PostgreSQL database adapter for Python
#         conn = psycopg.connect(host='localhost', dbname='py_api', user='postgres', password='Declan3245!', row_factory=dict_row)
#         cursor = conn.cursor()
#         print("Database connection was successful.")
#         break
#     except Exception as error:
#         print("Connecting to datbase failed.")
#         print("Error:", error)
#         time.sleep(2)
