from pydantic import BaseModel

class ConnectionString(BaseModel):

    scheme : str
    user_name : str | None = None
    password : int | None = None
    host : str
    port : str | None = None
    path : str | None = None
    query_parameters : str | None = None