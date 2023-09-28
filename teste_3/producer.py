#!/usr/bin/env python
import pika
import socket
from decouple import config
from datetime import datetime

MQ_username = config('USERNAME')
MQ_password = config('PASSWORD')
MQ_hostname = config('HOSTNAME')
MQ_virtual_host_server = config('VIRTUAL_HOST_SERVER')
MQ_queue = config('QUEUE')
MQ_port = config('PORT',default=5672, cast=int)


message = socket.gethostname() + "|" + datetime.now().strftime('%d/%m/%Y-%H:%M:%S')


credentials = pika.PlainCredentials(username=MQ_username, password=MQ_password, erase_on_connect=True)
parameters = pika.ConnectionParameters(host=MQ_hostname, port=MQ_port, virtual_host=MQ_virtual_host_server, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue=MQ_queue)
channel.basic_publish(exchange='', routing_key=MQ_queue, body=message)
print(" [x] Sent '" + message + " '")
connection.close() 
