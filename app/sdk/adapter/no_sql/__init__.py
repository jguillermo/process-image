from abc import ABC, abstractmethod
class NoSqlStorage(ABC):

    @abstractmethod
    def persist(self, table, id, data):
        pass

    @abstractmethod
    def find_one_by(self, table, filter):
        pass
