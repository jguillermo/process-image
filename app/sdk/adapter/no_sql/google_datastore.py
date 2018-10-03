
from sdk.adapter.no_sql import NoSqlStorage

class GoogleDataStore(NoSqlStorage):
    def _get_client(self):
        return True

    def persist(self, table, id, data):

        return True

    def find_one_by(self, table, filters):

        return None
