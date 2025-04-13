from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from sqlmodel import select
from typing_extensions import TypedDict

from connection import init_db, get_session
from models.models import *
from models.public_models import ProfilePublic, BookPublic


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/profile_list", response_model=list[ProfilePublic])
def get_profile_list(session=Depends(get_session)):
    return session.exec(select(Profile)).all()


@app.get("/profile/{profile_id}", response_model=ProfilePublic)
def get_profile(profile_id: int, session=Depends(get_session)):
    profile = session.get(Profile, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@app.post("/profile")
def create_profile(profile: ProfileDefault, session=Depends(get_session)) -> TypedDict("Response", {"status": int, "created": Profile}):
    profile = Profile.model_validate(profile)
    session.add(profile)
    session.commit()
    session.refresh(profile)
    return {"status": 201, "created": profile}


@app.patch("/profile/{profile_id}")
def update_profile(profile_id: int, upd_profile: ProfileDefault, session=Depends(get_session)) -> TypedDict("Response", {"status": int, "updated": Profile}):
    profile = session.get(Profile, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    upd_data = upd_profile.model_dump(exclude_unset=True)
    for key, value in upd_data.items():
        setattr(profile, key, value)
    session.commit()
    session.refresh(profile)
    return {"status": 200, "updated": profile}


@app.delete("/profile/{profile_id}")
def delete_profile(profile_id: int, session=Depends(get_session)) -> TypedDict("Response", {"status": int, "msg": str}):
    profile = session.get(Profile, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    session.delete(profile)
    session.commit()
    return {"status": 204, "msg": "Profile deleted"}


@app.get("/book_instance/{book_id}", response_model=BookPublic)
def get_book_instance(book_id: int, session=Depends(get_session)):
    book = session.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/book_instance")
def create_book_instance(new_book: BookDefault, session=Depends(get_session)) -> TypedDict("Response", {"status": int, "created": Book}):
    new_book = Book.model_validate(new_book)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return {"status": 201, "created": new_book}


@app.post("/book_info")
def create_book_info(book: BookInfoDefault, session=Depends(get_session)) -> TypedDict("Response", {"status": int, "created": BookInfo}):
    book = BookInfo.model_validate(book)
    session.add(book)
    session.commit()
    session.refresh(book)
    return {"status": 201, "created": book}
