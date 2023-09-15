from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app=FastAPI()

class Blog(BaseModel):
    title:str
    body:str
    published_at:Optional[bool]
    

@app.get('/blog')
async def index(limit,published:bool):
    if published:
     return {"Data":f'{limit} published blogs from the database list'}
    else:
        return {"Data":f'{limit}   blogs from the database list'}


@app.get('/blog/unpublished')
async def unpublished():
    return {"data":"All unpublished blogs"}

@app.get('/blog/{id}')
async def get_blog(id:int):
    return {"Data":id}




@app.get('/about')
async def about():
    return {"data":"This is About Page"}

@app.get('/blog/{id}/comments')
async def get_comments(id:int):
    return {"data":{"1","2"}}


#This is The example of Blog Request Body
@app.post('/blog')
async def create_blog(request:Blog):
    return {"data":f"Blog is created with title as{request.title}"}


# if __name__=="__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)
