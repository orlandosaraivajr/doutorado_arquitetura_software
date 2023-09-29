#!/usr/bin/env python
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy import text

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')

PG_NAME = config('PG_NAME')
PG_USER = config('PG_USER')
PG_PASSWORD = config('PG_PASSWORD')
PG_HOST = config('PG_HOST')

SQL_CREATE = "CREATE TABLE carros2 (id INTEGER, placa VARCHAR(20))"


DB_CONN = "mysql+mysqlconnector://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + "/" + DB_NAME
engine = create_engine(DB_CONN)
with engine.connect() as connection:
    connection.execute(text(SQL_CREATE))
    connection.commit()

DB_CONN2 = "postgresql+psycopg2://" + PG_USER + ":" + PG_PASSWORD + "@" + PG_HOST + "/" + PG_NAME
engine2 = create_engine(DB_CONN2)
with engine2.connect() as connection:
    connection.execute(text(SQL_CREATE))
    connection.commit()