from fastapi import FastAPI
from blackbird.blackbird import Blackbird

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Blackbird API running on Railway"}

@app.get("/search")
async def search(query: str):
    bb = Blackbird(query)
    results = bb.run()
    return {"results": results}