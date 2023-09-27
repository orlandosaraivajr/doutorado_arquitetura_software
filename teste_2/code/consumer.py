#!/usr/bin/env python
import pika, sys, os
from decouple import config

username = config('USERNAME')
password = config('PASSWORD')
hostname = config('HOSTNAME')
virtual_host_server = config('VIRTUAL_HOST_SERVER')
queue = config('QUEUE')


# Here we define the main script that will be executed forever until a keyboard interrupt exception is received
def main():
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(host=hostname, port=5672, virtual_host=virtual_host_server, credentials=credentials)
    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    
    # Since RabbitMQ works asynchronously, every time you receive a message, a callback function is called. We will simply print the message body to the terminal 
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # Consume a message from a queue. The auto_ack option simplifies our example, as we do not need to send back an acknowledgement query to RabbitMQ which we would normally want in production
    channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    # Start listening for messages to consume
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
