import os
from uri_builder import UriBuilder
from fastapi import FastAPI
from manager import Manager
from fast_api import FastApiEndpoint

scheme = os.getenv("SCHEME")
user_name = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")
path = os.getenv("PATH")
query_parameters = os.getenv("QUERY_PARAMETERS")

db_col = os.getenv("PATH", None)
col_name = os.getenv("COL_NAME", None)

connection_string = UriBuilder.build(scheme, user_name, password, host, port, path, query_parameters)

app = FastAPI
app_manager = Manager

fast_api_endpoint = FastApiEndpoint(FastAPI, app_manager)