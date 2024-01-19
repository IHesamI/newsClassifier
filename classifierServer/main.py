from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()


class News(BaseModel):
    text: str
    title: Union[str, None]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def getText(example:News):
    return {"message": "Hello World"}
