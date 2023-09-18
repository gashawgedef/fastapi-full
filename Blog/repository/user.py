


from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from .. import schemas
from ..hashing import Hash


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")



from .. import models


# def get_all_users(db:Session):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"the user with id {id} is not available",
#         )
#     return user

def get_single_user(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the user with id {id} is not available",
        )
    return user


def create_new_user(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
