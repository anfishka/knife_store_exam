from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..core.security import create_access_token, authenticate_user
from pydantic import BaseModel

class LoginData(BaseModel):
    username: str
    password: str

router = APIRouter()

@router.post("/login")
def login(data: LoginData, db: Session = Depends(get_db)):
    user = authenticate_user(db, data.username, data.password)
    if not user:
        raise HTTPException(400, "Invalid credentials")
    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}
