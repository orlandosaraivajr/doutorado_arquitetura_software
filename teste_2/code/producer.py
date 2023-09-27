#!/usr/bin/env python
import pika
import socket
from decouple import config

MQ_username = config('USERNAME')
MQ_password = config('PASSWORD')
MQ_hostname = config('HOSTNAME')
MQ_virtual_host_server = config('VIRTUAL_HOST_SERVER')
MQ_queue = config('QUEUE')
MQ_port = config('PORT',default=5672, cast=int)

# If you want to have a more secure SSL authentication, use ExternalCredentials object instead
credentials = pika.PlainCredentials(username=MQ_username, password=MQ_password, erase_on_connect=True)
parameters = pika.ConnectionParameters(host=MQ_hostname, port=MQ_port, virtual_host=MQ_virtual_host_server, credentials=credentials)

# We are using BlockingConnection adapter to start a session. It uses a procedural approach to using Pika and has most of the asynchronous expectations removed
connection = pika.BlockingConnection(parameters)
# A channel provides a wrapper for interacting with RabbitMQ
channel = connection.channel()

# Check for a queue and create it, if necessary
channel.queue_declare(queue=MQ_queue)

message = socket.gethostname()

# For the sake of simplicity, we are not declaring an exchange, so the subsequent publish call will be sent to a Default exchange that is predeclared by the broker
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(" [x] Sent '" + message + " '")

# Safely disconnect from RabbitMQ
connection.close() 
