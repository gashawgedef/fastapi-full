from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database
from ..database import get_db
from typing import List
from ..repository import blog

router = APIRouter(prefix="/blog", tags=["blogs"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create_new_blogs(request, db)


@router.get("/", response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db)):
    return blog.get_all_blogs(db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id, db: Session = Depends(get_db)):
    return blog.delete_blog(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(id, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update_blog(id, request, db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    return blog.get_single_blog(id, db)
