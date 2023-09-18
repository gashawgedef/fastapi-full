from fastapi import APIRouter, Depends, HTTPException, Response, status, requests
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..database import get_db
from typing import List
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=["blogs"]
    
    
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create_new_blogs(request,db)
 


@router.get("/", response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(get_db)):
   return blog.get_all_blogs(db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return blog


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(id, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id  {id} is not avaialable",
        )
    blog.update(request.dict())
    db.commit()
    return "Updated successfully"


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(get_db)):
    data = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"the blog with id {id} is not available",
        )
        # response.status_code=status.HTTP_404_NOT_FOUND
        return {"detail": f"blog with the id  {id} is not avaialable"}
    return data
