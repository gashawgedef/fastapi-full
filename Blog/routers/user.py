from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..repository import user



router = APIRouter(prefix="/user", tags=["users"])


@router.post("/", response_model=schemas.ShowUser, tags=["users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_new_user(request, db)


@router.get("/{id}", response_model=schemas.ShowUser, tags=["users"])
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_single_user(id, db)
