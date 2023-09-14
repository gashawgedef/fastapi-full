from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def index():
    return {"Data":"Blog List"}


@app.get('/blog/{id}')
async def get_blog(id:int):
    return {"Data":id}


@app.get('/about')
async def about():
    return {"data":"This is About Page"}

@app.get('/blog/{id}/comments')
async def get_comments(id:int):
    return {"data":{"1","2"}}
