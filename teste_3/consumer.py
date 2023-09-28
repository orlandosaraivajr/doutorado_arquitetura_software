#!/usr/bin/env python
import pika, sys, os
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy import text

MQ_username = config('USERNAME')
MQ_password = config('PASSWORD')
MQ_hostname = config('HOSTNAME')
MQ_virtual_host_server = config('VIRTUAL_HOST_SERVER')
MQ_queue = config('QUEUE')
MQ_port = config('PORT', default=5672, cast=int)

DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')

DB_CONN = "mysql+mysqlconnector://" + DB_USER + ":" + DB_PASSWORD + "@" + DB_HOST + "/" + DB_NAME
engine = create_engine(DB_CONN)


def callback(ch, method, properties, body):
    print(" [x] Recebido %r" % body)
    body = body.decode().split('|')
    with engine.connect() as connection:
        sql = 'INSERT INTO Carros '
        sql = sql + '(placa)'
        sql = sql + 'VALUES ( \''
        sql = sql + body[0]
        sql = sql + '\')'
        print(sql)
        connection.execute(text(sql))
        connection.execute(text("INSERT INTO Carros (placa) VALUES (:placa)"), {"placa": body[0]})
        connection.commit()
        

def consume():
    credentials = pika.PlainCredentials(MQ_username, MQ_password)
    parameters = pika.ConnectionParameters(host=MQ_hostname, port=MQ_port, virtual_host=MQ_virtual_host_server, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=MQ_queue)
    channel.basic_consume(queue=MQ_queue, on_message_callback=callback, auto_ack=True)
    print('  Consumindo mensagens. Para sair pressione CTRL+C')
    
    # Start listening for messages to consume
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
