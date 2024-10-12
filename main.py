from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()
users = []

class User(BaseModel):
    id: str 
    balance: int = 0
    logs: str = ""

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

@app.get("/users/{id}", response_model=User)
def get_user(id: int)-> User:
    if (id >= len(users)):
        raise HTTPException(status_code=404, detail="user not found")
    return users[id]

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users.append(user)
    return users 

@app.put("/user/{id}")
def update_user(id: int):
    return "update user item with id {id}"

@app.delete("/user/{id}")
def delete_user(id: int):
    return "delete user item with id {id}"

@app.get("/users", response_model=list[User])
def get_users(limit: int = 10):
    return users[0:limit]