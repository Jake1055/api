from typing import List
from pydantic import BaseModel, Field, field_validator
from pydantic_core import PydanticCustomError

__all__ = ["IncomingBook", "ReturnedAllBooks", "ReturnedBook", "UpdatedBook", "ReturnedBookForSeller"]

class BaseBook(BaseModel):
    title: str
    author: str
    year: int

class BookWithSeller(BaseModel):
    seller_id: int

class ValidationIncomingBook(BaseBook):
    year: int = 2024
    count_pages: int = Field(
        alias="pages",
        default=1,
    ) 

    @field_validator("year") 
    @staticmethod
    def validate_year(val: int):
        if val < 1400:
            raise PydanticCustomError("Validation error", "Year is wrong!")
        return val

    class Config:
        populate_by_name = True

class IncomingBook(ValidationIncomingBook, BookWithSeller):
    pass

class ReturnedBook(BaseBook, BookWithSeller):
    id: int
    count_pages: int = 0

    class Config:
        from_attributes = True


class UpdatedBook(ValidationIncomingBook):
    pass

class ReturnedAllBooks(BaseModel):
    books: List[ReturnedBook]

    class Config:
        from_attributes = True

class ReturnedBookForSeller(ReturnedBook):
    seller_id: int = Field(exclude=True)

    class Config:
        from_attributes = True
