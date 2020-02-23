import json
import pika

from src.config.rabbitmq import RBMQSettings
from src.utils.logger import logger


class RabbitMQ:

    def __init__(self):
        self.config = RBMQSettings()

    def _set_connection(self):
        credentials = pika.PlainCredentials(self.config.USER, self.config.PASS)
        parameters = pika.ConnectionParameters(host=self.config.HOST, credentials=credentials,
                                               port=self.config.PORT)
        connection = pika.BlockingConnection(parameters)

        return connection

    def insert(self, data):
        logger.info(f'Insert data on {self.config.CALC_QUEUE}')

        conn = self._set_connection()
        channel = conn.channel()
        channel.queue_declare(queue=self.config.CALC_QUEUE)
        channel.basic_publish(exchange='', routing_key=self.config.CALC_QUEUE, body=json.dumps(data.serialize()))
        conn.close()

        logger.info(f'Data inserted')


rbmq = RabbitMQ()
