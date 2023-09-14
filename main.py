from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def index():
    return {"Data":{"name":"Welcome Gashity"}}