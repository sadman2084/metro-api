from pydantic import BaseModel

class User(BaseModel):
    key: str 
    balance: int = 0
    logs: str = ""