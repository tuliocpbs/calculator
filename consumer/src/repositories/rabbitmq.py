import json
import pika
import time

from src.config.rabbitmq import RBMQConfig


class RabbitMQ:

    def __init__(self):
        self.config = RBMQConfig()
        self.conn = self._set_connection()

    def _set_connection(self):
        credentials = pika.PlainCredentials(self.config.USER, self.config.PASS)
        parameters = pika.ConnectionParameters(host=self.config.HOST, credentials=credentials,
                                                port=self.config.PORT)
        connection = pika.BlockingConnection(parameters)

        return connection

    def insert_deadqueue(self, data):
        channel = self.conn.channel()
        channel.queue_declare(queue=self.config.DEADQUEUE)
        channel.basic_publish(exchange='', routing_key=self.config.DEADQUEUE, body=json.dumps(data))


rbmq = RabbitMQ()
