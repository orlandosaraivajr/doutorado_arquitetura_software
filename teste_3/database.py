#!/usr/bin/env python
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy import text

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')

DB_CONN = "mysql+mysqlconnector://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + "/" + DB_NAME
engine = create_engine(DB_CONN)

with engine.connect() as connection:
    connection.execute(text("CREATE TABLE Carros (id INTEGER, placa VARCHAR(20))"))