import pymongo
import pandas as pd

from gthrytgse import my_client


class Fetcher:

    def __init__(self, scheme, host, user_name = None, password = None, port = None, path = None, query_parameters = None):
        connection_string = Fetcher.connection_string_builder(scheme, user_name, password, host, port, path, query_parameters)
        self.my_client = pymongo.MongoClient(connection_string)



    @staticmethod
    def connection_string_builder(scheme, user_name, password, host, port, path, query_parameters):
        connection_string = scheme + "://"

        if user_name or password:
            if user_name:
                connection_string += user_name
            if password:
                connection_string += ':' + password + '@'
            else:
                connection_string += '@'

        connection_string += host

        if port:
            connection_string += ':' + port

        if path:
            connection_string += '/' + path

        if query_parameters:
            connection_string += '?' + query_parameters

        return connection_string



















