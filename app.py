from typing import Union

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from princebreaker import prince_break

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    name: str ="GUEDJE Prince Gédéon"

@app.on_event("startup")
def on_startup():
    # Don't forget to declare pipe as a global variable
    load_dotenv()

@app.post("/research")
def read_root(input:Input):
    """
    Icebreaker by name
    :param input:
    :return:
    """
    output,url=prince_break(input.name)
    return {"summary": output.summary,"facts": output.facts,"topics":output.topics_of_interest,"ice_breaker":output.ice_breaker,"picture_url":url }
