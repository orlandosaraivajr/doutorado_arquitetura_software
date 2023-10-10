#!/usr/bin/env python
import pika
from decouple import config
import requests

MQ_username = config('USERNAME')
MQ_password = config('PASSWORD')
MQ_hostname = config('HOSTNAME')
MQ_virtual_host_server = config('VIRTUAL_HOST_SERVER')
MQ_queue = config('QUEUE')
MQ_port = config('PORT',default=5672, cast=int)
URL = config('URL')


class FrankException(BaseException):
    pass


def consumir_API(URL):
    try:
        req = requests.get(URL)
    except:
        raise FrankException('Erro ao Consumir API')
    dados = req.json()
    return dados

credentials = pika.PlainCredentials(username=MQ_username, password=MQ_password, erase_on_connect=True)
parameters = pika.ConnectionParameters(host=MQ_hostname, port=MQ_port, virtual_host=MQ_virtual_host_server, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue=MQ_queue)

for r in consumir_API(URL):
    message = str(r.get('id')) + '|' + r.get('placa') + '|'
    message += r.get('portaria') + '|' + r.get('tipo') + '|'
    message += r.get('data') + '|' + r.get('hora') + '|'

    channel.basic_publish(exchange='', routing_key=MQ_queue, body=message)
    print(" [x] Enfileirado '" + message + " '")

connection.close() 
