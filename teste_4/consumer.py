#!/usr/bin/env python
import pika, sys, os
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy import text

# RabbitMQ credentials
MQ_username = config('USERNAME')
MQ_password = config('PASSWORD')
MQ_hostname = config('HOSTNAME')
MQ_virtual_host_server = config('VIRTUAL_HOST_SERVER')
MQ_queue = config('QUEUE')
MQ_port = config('PORT', default=5672, cast=int)
# MySQL credentials
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
# PostgreSQL credentials
PG_NAME = config('PG_NAME')
PG_USER = config('PG_USER')
PG_PASSWORD = config('PG_PASSWORD')
PG_HOST = config('PG_HOST')

DB_CONN = "mysql+mysqlconnector://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + "/" + DB_NAME
engine = create_engine(DB_CONN)
PG_CONN = "postgresql+psycopg2://" + PG_USER + ":" + PG_PASSWORD + "@" + PG_HOST + "/" + PG_NAME
PG_engine = create_engine(PG_CONN)

def write_MySQL(placa):
    with engine.connect() as connection:
        connection.execute(text("INSERT INTO Carros (placa) VALUES (:placa)"), {"placa": placa})
        connection.commit()

def write_PostgreSQL(placa):
    with PG_engine.connect() as connection:
        connection.execute(text("INSERT INTO Carros (placa) VALUES (:placa)"), {"placa": placa})
        connection.commit()

def callback(ch, method, properties, body):
    print(" [x] Recebido %r" % body)
    body = body.decode().split('|')
    write_MySQL(body[0])
    write_PostgreSQL(body[0])
        

def consume():
    credentials = pika.PlainCredentials(MQ_username, MQ_password)
    parameters = pika.ConnectionParameters(host=MQ_hostname, port=MQ_port, virtual_host=MQ_virtual_host_server, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=MQ_queue)
    channel.basic_consume(queue=MQ_queue, on_message_callback=callback, auto_ack=True)
    print('  Consumindo mensagens. Para sair pressione CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        consume()
    except KeyboardInterrupt:
        print("Interrompido")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
