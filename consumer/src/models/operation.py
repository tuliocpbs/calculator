import operator
from functools import reduce

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.utils.logger import logger


base = declarative_base()


class CalculatorResult(base):
    __tablename__ = 'result'
    delivery_tag = Column(Integer, primary_key=True)
    result = Column(Float)
    msg = Column(String(300))

    def __init__(self, delivery_tag=None, function=None, arguments=None):
        self.delivery_tag = delivery_tag
        self.result, self.msg = self.execute_operation(function, arguments)

    def execute_operation(self, function, arguments):
        logger.info(f'Delivery tag: {self.delivery_tag}, Executing {function} over {arguments} arguments')

        try:
            if function == 'sum':
                return sum(arguments), 'Executed with success'
            elif function == 'subtract':
                return reduce((lambda x, y: x - y), arguments), 'Executed with success'
            elif function == 'multiply':
                return reduce((lambda x, y: x * y), arguments), 'Executed with success'
            if function == 'divide':
                return reduce((lambda x, y: x / y), arguments), 'Executed with success'
        
        except Exception as e:
            logger.error(f'Delivery tag: {self.delivery_tag}, Error: {repr(e)}')
            return None, f'Operation failed, error {repr(e)}'
