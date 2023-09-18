
from  fastapi import APIRouter,Depends, HTTPException, Response,status,requests
from sqlalchemy.orm import Session
from .. import schemas,database ,models
from ..database import get_db
from typing import List
from passlib.context import CryptContext
from ..hashing import Hash

router=APIRouter()


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/user", response_model=schemas.ShowUser, tags=["users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    # hashed_password=pwd_cxt.hash(request.password)
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# get a single user
@router.get("/user/{id}", response_model=schemas.ShowUser, tags=["users"])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the user with id {id} is not available",
        )
    return user
