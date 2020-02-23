from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config.postgresql import PostgreSQLConfig


class Postgresql:
    def __init__(self):
        self.config = PostgreSQLConfig()
        self.db = self._create_engine()

    def _create_engine(self):
        db_string = f'postgresql://{self.config.USER}:{self.config.PASS}@{self.config.HOST}:{self.config.PORT}/calculator'
        return create_engine(db_string)

    def _set_session(self):
        Session = sessionmaker(self.db)
        return Session()

    def insert(self, operation):
        session = self._set_session()
        session.add(operation)
        session.commit()


postgsql = Postgresql()
