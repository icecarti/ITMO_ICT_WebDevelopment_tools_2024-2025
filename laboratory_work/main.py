from fastapi import FastAPI
from typing import List
from typing_extensions import TypedDict
from models import Profile
from mock import mock_db

app = FastAPI()


class CreateResponse(TypedDict):
    status: int
    data: Profile


class UpdateResponse(TypedDict):
    status: int
    data: Profile


class DeleteResponse(TypedDict):
    status: int
    message: str


@app.get("/")
def root():
    return {"message": "Welcome to the Profile API"}


@app.get("/profile_list", response_model=List[Profile])
def profile_list():
    return mock_db


@app.get("/profile/{profile_id}", response_model=Profile)
def profile_get(profile_id: int):
    for profile in mock_db:
        if profile["id"] == profile_id:
            return profile
    return {"message": "Profile not found"}


@app.post("/profile", response_model=CreateResponse)
def profile_create(profile: Profile):
    new_profile = profile.model_dump()
    mock_db.append(new_profile)
    return {"status": 201, "data": profile}


@app.put("/profile/{profile_id}", response_model=UpdateResponse)
def profile_update(profile_id: int, updated_profile: Profile):
    for i, profile in enumerate(mock_db):
        if profile["id"] == profile_id:
            mock_db[i] = updated_profile.model_dump()
            return {"status": 205, "data": updated_profile}
    return {"status": 404, "data": updated_profile}


@app.delete("/profile/{profile_id}", response_model=DeleteResponse)
def profile_delete(profile_id: int):
    for i, profile in enumerate(mock_db):
        if profile["id"] == profile_id:
            mock_db.pop(i)
            return {"status": 202, "message": "deleted"}
    return {"status": 404, "message": "Profile not found"}
