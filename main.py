from typing import Literal
from fastapi import Depends, FastAPI, HTTPException, Request, status
from sqlalchemy import update
from database import Base, engine, SessionLocal
from fastapi.responses import RedirectResponse
import models
import schemas
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)  # creating database
app = FastAPI()  # app init
users = []

# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

@app.get("/users/{id}")
def get_user_balance(key: str, session: Session = Depends(get_session)) -> int:
    user = session.query(models.User).filter(models.User.key == key).first()
    if not user:
        new_user = schemas.User(key=key, balance=0, logs="")
        create_new_user(new_user, session)
        return 0
    return session.query(models.User).filter(models.User.key == key).with_entities(models.User.balance).scalar()

@app.get("/users")
def get_all_users(session: Session = Depends(get_session)):
    user_data = session.query(models.User).all()
    return user_data

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_new_user(user: schemas.User, session: Session = Depends(get_session)):
    user_db = models.User(key=user.key, balance=user.balance, logs=user.logs)
    
    # add it to the session and commit it
    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return user_db

@app.put("/users/+/{id}")
def user_balance_recharge(key: str, val: int, session: Session = Depends(get_session)):
    user = session.query(models.User).filter(models.User.key == key).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"user {key} not found")
    
    # Update the balance
    session.execute(
        update(models.User).where(models.User.key == key).values(balance=user.balance + int(val))
    )
    session.commit()
    return {"message": "Balance recharged successfully"}

@app.put("/users/-/{id}")
def user_balance_discharge(key: str, val: int, session: Session = Depends(get_session)):
    current_balance = get_user_balance(key=key, session=session)
    if current_balance < val:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    user = session.query(models.User).filter(models.User.key == key).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"user {key} not found")
    
    # Update the balance
    session.execute(
        update(models.User).where(models.User.key == key).values(balance=user.balance - int(val))
    )
    session.commit()
    return {"message": "Balance discharged successfully"}

@app.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(key: str, session: Session = Depends(get_session)):
    user = session.query(models.User).filter(models.User.key == key).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"user {key} not found")
    session.delete(user)
    session.commit()
