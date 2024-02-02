from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
import json


from classifierClass import textClassifier

myClassifier = textClassifier()


app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class News(BaseModel):
    text: str
    title: Union[str, None]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def getText(request: Request):
    result = await request.body()
    body: News = json.loads(result)
    text = body['text']
    result = myClassifier.predict(text)
    return result
