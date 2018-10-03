# -*- coding: utf-8 -*-
import dependency_injector.containers as containers
import dependency_injector.providers as providers
from bootstrap.config import FileConfig
from sdk.adapter.encryption.jwt import JwtEncrypt
from sdk.adapter.log.logging import ConsoleLogger
from sdk.adapter.sql.sqlalchemy import SqlAlchemyAdapter, SqlAlchemySearchAdapter, SqlAlchemySession


class LoggerInjector(containers.DeclarativeContainer):
    console = providers.Singleton(ConsoleLogger)


class ConfigDI:
    @staticmethod
    def file():
        return FileConfig()


class AdapterSqlAlchemyDI:
    @staticmethod
    def alchemy_session():
        return SqlAlchemySession(config=ConfigDI.file())

    @staticmethod
    def search():
        return SqlAlchemySearchAdapter(sql_alchemy_session=AdapterSqlAlchemyDI.alchemy_session())

    @staticmethod
    def orm():
        return SqlAlchemyAdapter(sql_alchemy_session=AdapterSqlAlchemyDI.alchemy_session())

class EncryptDI:
    @staticmethod
    def jwt():
        return JwtEncrypt()




class AdapterInjector(containers.DeclarativeContainer):
    """
    Adapter
    """
    sql_alchemy = providers.Factory(SqlAlchemyAdapter, sql_alchemy_session=AdapterSqlAlchemyDI.alchemy_session())
