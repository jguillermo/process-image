# -*- coding: utf-8 -*-
from sqlalchemy import create_engine, text
from sqlalchemy.engine import ResultProxy
from sqlalchemy.orm import sessionmaker, scoped_session
from sdk.adapter.config.base import BaseConfig
from sdk.automation import Singleton


class SqlAlchemySession(metaclass=Singleton):
    _session = None
    _engine = None

    def __init__(self, config: BaseConfig):
        self._options = config.get_key('database')

    def get_engine(self):
        if self._engine is None:
            try:
                driver = '{}?charset=utf8'.format(self._options['url'])
                self._engine = create_engine(driver, echo=self._options['log'], isolation_level="READ UNCOMMITTED")
            except Exception as e:
                raise e
        return self._engine

    def get_session(self):
        if self._session is None:
            try:
                Session = sessionmaker(bind=self.get_engine())
                self._session = Session()
            except Exception as e:
                raise e
        return self._session

    def close(self):
        if self._session is not None:
            self.get_session().close()
            self._session = None

        if self._engine is not None:
            self.get_engine().dispose()
            self._engine = None


class SqlAlchemyAdapter:
    _entity = None

    def __init__(self, sql_alchemy_session: SqlAlchemySession):
        self.sql_alchemy_session = sql_alchemy_session

    def persist(self, entity):
        session = self.sql_alchemy_session.get_session()
        try:
            session.add(entity)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            self.sql_alchemy_session.close()
            raise e

    def find_by_id(self, id):
        session = self.sql_alchemy_session.get_session()
        try:
            return session.query(self._entity).filter_by(id=id).first()
        except Exception as e:
            session.rollback()
            self.sql_alchemy_session.close()
            raise e


class SqlAlchemySearchAdapter:

    def __init__(self, sql_alchemy_session: SqlAlchemySession):
        self.sql_alchemy_session = sql_alchemy_session

    def query(self, sql_str: str, params=None) -> ResultProxy:
        try:
            result = self.sql_alchemy_session.get_engine().execute(sql_str)
            self.sql_alchemy_session.close()
            return result.fetchall()
        except Exception as e:
            raise e

    def result(self, sql_str: str, params=None):
        result = self.query(sql_str, params)
        data = []
        for row in result:
            row_value = {}
            for value in row.keys():
                row_value[value] = row[value]
            data.append(row_value)
        return data
