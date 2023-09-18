from fastapi import APIRouter, Depends, HTTPException, Response, status, requests
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..database import get_db
from typing import List

from .. repository import user
router = APIRouter(prefix="/user", tags=["users"])


@router.post("/", response_model=schemas.ShowUser, tags=["users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_new_user(request,db)
    # hashed_password=pwd_cxt.hash(request.password)
 

# get a single user
@router.get("/{id}", response_model=schemas.ShowUser, tags=["users"])
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_single_user(id,db)
