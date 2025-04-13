from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from .default_models import *

class BookTagLink(SQLModel, table=True):
    info_id: Optional[int] = Field(default=None, foreign_key="bookinfo.id", primary_key=True)
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)

class BookInfo(BookInfoDefault, table=True):
    id: int = Field(default=None, primary_key=True)
    tags: Optional[list["Tag"]] = Relationship(back_populates="books", link_model=BookTagLink)
    instances: Optional[list["Book"]] = Relationship(back_populates="info")

class Book(BookDefault, table=True):
    id: int = Field(default=None, primary_key=True)
    info: Optional[BookInfo] = Relationship(back_populates="instances")
    owner: Optional["Profile"] = Relationship(back_populates="books")

class Profile(ProfileDefault, table=True):
    id: int = Field(default=None, primary_key=True)
    books: Optional[list[Book]] = Relationship(back_populates="owner")

class Tag(TagDefault, table=True):
    id: int = Field(default=None, primary_key=True)
    books: Optional[list[BookInfo]] = Relationship(back_populates="tags", link_model=BookTagLink)

class ShareRequest(ShareRequestDefault, table=True):
    id: int = Field(default=None, primary_key=True)
