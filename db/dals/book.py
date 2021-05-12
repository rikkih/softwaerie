from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.book import Book


class BookDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_book(self, name: str, author: str, release_year: int):
        book = Book(name=name, author=author, release_year=release_year)
        self.db_session.add(book)
        await self.db_session.flush()

