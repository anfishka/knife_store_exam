from datetime import datetime, timedelta
from jose import jwt
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.settings import settings
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(user_id: int, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = {"sub": str(user_id), "exp": datetime.utcnow() + expires_delta}
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None

def get_current_admin_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(401, "Invalid token")
    except:
        raise HTTPException(401, "Invalid token")

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user or user.role != "admin":
        raise HTTPException(403, "Not an admin")
    return user
