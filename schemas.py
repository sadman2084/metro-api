from pydantic import BaseModel

class User(BaseModel):
    id: str 
    balance: int = 0
    logs: str = ""