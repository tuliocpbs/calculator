import os
import sys
import socket

from logger import logger


POSTSQL_HOST = os.environ.get('POSTSQL_HOST')
POSTSQL_PORT = os.environ.get('POSTSQL_PORT')
RBMQ_HOST = os.environ.get('RBMQ_HOST')
RBMQ_PORT = os.environ.get('RBMQ_PORT')


class Healthcheck:

    def check(self):
        logger.info('Checking PostgreSQL and RabbitMQ health')
        postgres_health = self._check_postgres_health(POSTSQL_HOST, POSTSQL_PORT)

        rbmq_health = self._check_rbmq_health(RBMQ_HOST, RBMQ_PORT)

        logger.info(f'PostgreSQL: {postgres_health} and RabbitMQ: {rbmq_health}')
        if postgres_health and rbmq_health:
            return True
        else:
            return False

    def _check_postgres_health(self, ip, port):
        return self._is_open(ip, port)

    def _check_rbmq_health(self, ip, port):
        return self._is_open(ip, port)

    def _is_open(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
           s.connect((ip, int(port)))
           s.shutdown(2)
           return True
        except:
           return False


if __name__ == '__main__':
    health = Healthcheck()
    if health.check():
        sys.exit(0)
    else:
        sys.exit(1)
