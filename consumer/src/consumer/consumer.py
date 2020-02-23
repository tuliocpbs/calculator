import json

from src.models.operation import CalculatorResult
from src.repositories.postgresql import postgsql
from src.repositories.rabbitmq import rbmq
from src.utils.logger import logger


class ConsumersManager:

    def __init__(self):
        self._channel = rbmq.conn.channel()
        self.queue = rbmq.config.CALC_QUEUE
        self._declare_channels()

    def _declare_channels(self):
        self._channel.queue_declare(queue=self.queue)

    def set_consumers(self):
        Consumer(self._channel, self.queue)

    def start_consumers(self):
        logger.info('Starting Consumers...')

        try:
            self._channel.start_consuming()
        except KeyboardInterrupt:
            self._channel.stop_consuming()

        rbmq.conn.close()


class Consumer:

    def __init__(self, channel, queue):
        self.ch = channel
        self.queue = queue
        self._consumer_tag = None
        self._set_consumer()

    def _set_consumer(self):
        logger.info(f'Set Consumer for {self.queue} queue')

        self._consumer_tag = self.ch.basic_consume(self.queue, self._callback)

        logger.info(f'Consumer tag: {self._consumer_tag}')

    def _callback(self, channel, method_frame, header_frame, data):
        #TODO: Ensure no side effects for Consumers
        logger.info(f'Delivery tag: {method_frame.delivery_tag}')
        try:
            operation = json.loads(data.decode('utf-8'))
            
            calc_op = CalculatorResult(delivery_tag=method_frame.delivery_tag,
                                        function=operation['function'],
                                        arguments=operation['arguments'])

            postgsql.insert(calc_op)

        except Exception as e:
            # If a unexpected error occurs send the data for a deadqueue for a future analysis
            logger.error(f'Delivery tag: {method_frame.delivery_tag}, Error: {repr(e)}')
            rbmq.insert_deadqueue(operation)
        
        finally:
            logger.info(f"Delivery tag: {method_frame.delivery_tag}, Finished ack")
            self.ch.basic_ack(delivery_tag=method_frame.delivery_tag)
