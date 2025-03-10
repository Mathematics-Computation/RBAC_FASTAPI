from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from auth import get_current_user, require_role
from models import User

router = APIRouter()

@router.get("/profile")
def profile(user: User = Depends(get_current_user)):
    return {"username": user.username, "role": user.role.name}

@router.get("/all-users", dependencies=[Depends(require_role("admin"))])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
