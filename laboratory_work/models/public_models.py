from typing import Optional
from .default_models import ProfileDefault, BookDefault, ShareRequestDefault

class ProfilePublic(ProfileDefault):
    id: int
    books: Optional[list[BookDefault]] = []

class BookPublic(BookDefault):
    id: int
