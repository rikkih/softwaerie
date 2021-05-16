from fastapi import FastAPI
import uvicorn

from db.config import async_session
from db.dals import BookDAL

app = FastAPI()


@app.post("/books")
async def create_book(name: str, author: str, release_year: str):
    async with async_session() as session:
        async with session.begin():
            book_dal = BookDAL(session)
