from abc import ABC, abstractmethod

class FetcherABC(ABC):

    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.my_client = None

    @abstractmethod
    def open_connection(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    @abstractmethod
    def get_database_names(self):
        pass

    @abstractmethod
    def get_dataset_names(self):
        pass

    @abstractmethod
    def get_field_names(self, db_name, col_name):
        pass

    @abstractmethod
    def get_collection_data(self, db_name, col_name):
        pass