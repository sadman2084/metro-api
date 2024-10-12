from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import RedirectResponse
import schemas

app = FastAPI()
users = []

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

@app.get("/users/{id}", response_model=schemas.User)
def get_user(id: int)-> schemas.User:
    if (id >= len(users)):
        raise HTTPException(status_code=404, detail="user not found")
    return users[id]

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.User):
    users.append(user)
    return users 

@app.put("/user/{id}")
def update_user(id: int):
    return "update user item with id {id}"

@app.delete("/user/{id}")
def delete_user(id: int):
    return "delete user item with id {id}"

@app.get("/users", response_model=list[schemas.User])
def get_users(limit: int = 10):
    return users[0:limit]