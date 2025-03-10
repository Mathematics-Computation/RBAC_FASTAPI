from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from auth import authenticate_user, create_access_token, hash_password
from database import get_db
from models import User, Role

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register")
def register(username: str, password: str, role_name: str, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.name == role_name).first()
    if not role:
        raise HTTPException(status_code=400, detail="Role does not exist")

    user = User(username=username, hashed_password=hash_password(password), role_id=role.id)
    db.add(user)
    db.commit()
    return {"message": "User registered successfully"}
