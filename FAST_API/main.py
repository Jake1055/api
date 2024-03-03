from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title = 'Library with books',
    description='Описание приложения',
    version = '0.0.1',
    responses= {404: {'description':'Not Found'}}

)

fake_storage = []

class Book(BaseModel):
    name: str
    author: str
    year: int | None = None




@app.get('/', include_in_schema=False)
async def main():
    return 'Hello world!' 


@app.post('/books/')
async def create(book: Book):
    new_book = {'name': book.name, 'author': book.author, 'year': book.year}
    fake_storage.append(new_book)
    return new_book

@app.get('/books/')
async def get_all_books():
    return fake_storage