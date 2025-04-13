from fastapi import FastAPI, Depends
from sqlmodel import select
from typing_extensions import TypedDict
from contextlib import asynccontextmanager

from connection import init_db, get_session
from models.models import *
from models.public_models import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"status": "API is alive"}

@app.get("/profiles", response_model=list[ProfilePublic])
def list_profiles(session=Depends(get_session)):
    return session.exec(select(Profile)).all()
