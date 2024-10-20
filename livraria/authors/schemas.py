from pydantic import BaseModel


class AuthorBase(BaseModel):
    nome: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class ConfigDict:
        from_attributes = True


class AuthorItems(BaseModel):
    items: list[Author]
