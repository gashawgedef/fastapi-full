from fastapi import FastAPI

app=FastAPI()

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
