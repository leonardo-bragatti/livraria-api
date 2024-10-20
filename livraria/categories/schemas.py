from pydantic import BaseModel


class CategoryBase(BaseModel):
    nome: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class ConfigDict:
        from_attributes = True


class CategoryItems(BaseModel):
    items: list[Category]
