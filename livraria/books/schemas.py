from typing import Optional

from pydantic import BaseModel, Field


class BookBase(BaseModel):
    titulo: str
    isbn: str
    capa: str
    ano: int
    paginas: int


class BookCreate(BookBase):
    publisher_id: int = Field(alias="editoraId")
    category_id: int = Field(alias="categoriaId")
    author_id: Optional[int] = Field(alias="autorId")


class Book(BookBase):
    id: int

    class ConfigDict:
        from_attributes = True


class BookItems(BaseModel):
    items: list[Book]
