# -*- coding: utf-8 -*-
from bootstrap.config import FileConfig
from sdk.adapter.encryption.jwt import JwtEncrypt
from sdk.adapter.log.logging import ConsoleLogger


class LoggerInjector(containers.DeclarativeContainer):
    console = providers.Singleton(ConsoleLogger)


class ConfigDI:
    @staticmethod
    def file():
        return FileConfig()


class EncryptDI:
    @staticmethod
    def jwt():
        return JwtEncrypt()

