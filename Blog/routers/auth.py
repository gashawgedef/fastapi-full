from fastapi import APIRouter, Depends, HTTPException, status

from .. import models

from .. import schemas, database,token
from .. hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(prefix="/login", tags=["Authentication"])


@router.post("/")
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid credentials",
        )
    
    if not  Hash.verify(user.password,request.password):
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Incorrect Password",
        )
    access_token=token.create_access_token(data={"sub":user.email})

    return {"access_token":access_token,"token_type":"bearer"}
