from requests import request
from sqlalchemy.orm import Session

from .. import schemas
from .. import models

def get_all_blogs(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create_new_blogs(request: schemas.Blog,db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog