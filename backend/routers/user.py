from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.user import UserCreate, UserResponse, UserLogin
from backend.crud.user import create_user, get_user_by_username
from backend.database import get_db
from backend.utils.security import verify_password

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user, error = create_user(db, user_in)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return user

@router.post("/login")
def login(user_in: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_username(db, user_in.username)     # Retrieve user by username
    if not user or not verify_password(user_in.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Login successful", "username": user.username}
