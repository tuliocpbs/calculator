import os


class PostgreSQLConfig:
    ''' Elasticsearch Settings
    '''
    HOST = os.environ.get('POSTSQL_HOST')
    PORT = os.environ.get('POSTSQL_PORT')
    USER = os.environ.get('POSTSQL_USER')
    PASS = os.environ.get('POSTSQL_PASSWORD')
    
    def __init__(self):
        self._validate_host()
        self._validate_port()
        self._validate_user()
        self._validate_pass()

    def _validate_host(self):
        if self.HOST is None:
            raise ValueError("POSTSQL_HOST should not be empty")

    def _validate_port(self):
        if self.PORT is None:
            raise ValueError("POSTSQL_PORT should not be empty")

    def _validate_user(self):
        if self.USER is None:
            raise ValueError("POSTSQL_USER should not be empty")

    def _validate_pass(self):
        if self.PASS is None:
            raise ValueError("POSTSQL_PASSWORD should not be empty")
