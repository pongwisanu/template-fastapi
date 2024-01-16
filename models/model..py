from pydantic import BaseModel

class UsersModel(BaseModel):
    name:str
    last:str