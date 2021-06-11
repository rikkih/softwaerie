from typing import Optional

from pydantic import BaseModel, UUID4


class PostBase(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None


# Properties to receive
class PostCreate(PostBase):
    title: str
    body: str


class PostUpdate(PostBase):
    pass


class PostInDBBase(PostBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Properties to return
class Post(PostInDBBase):
    pass


class PostInDB(PostInDBBase):
    pass

