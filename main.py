from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def index():
    return {"Data":"Blog List"}


@app.get('/about')
async def about():
    return {"data":"This is About Page"}