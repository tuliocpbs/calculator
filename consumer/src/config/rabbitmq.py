import os


class RBMQConfig:
    ''' RabbitMQ Settings
    '''
    HOST = os.environ.get('RBMQ_HOST')
    PORT = os.environ.get('RBMQ_PORT')
    USER = os.environ.get('RBMQ_USER')
    PASS = os.environ.get('RBMQ_PASS')
    CALC_QUEUE = os.environ.get('CALC_QUEUE')
    DEADQUEUE = os.environ.get('DEADQUEUE')

    def __init__(self):
        self._validate_host()
        self._validate_port()
        self._validate_user()
        self._validate_pass()
        self._validate_calc_queue()
        self._validate_deadqueue()

    def _validate_host(self):
        if self.HOST is None:
            raise ValueError("RBMQ_HOST should not be empty")
    
    def _validate_port(self):
        if self.PORT is None:
            raise ValueError("RBMQ_PORT should not be empty")

    def _validate_user(self):
        if self.USER is None:
            raise ValueError("RBMQ_USER should not be empty")

    def _validate_pass(self):
        if self.PASS is None:
            raise ValueError("RBMQ_PASS should not be empty")

    def _validate_calc_queue(self):
        if self.CALC_QUEUE is None:
            raise ValueError("CALC_QUEUE should not be empty")

    def _validate_deadqueue(self):
        if self.DEADQUEUE is None:
            raise ValueError("DEADQUEUE should not be empty")
