from pydantic import BaseModel


class PublisherBase(BaseModel):
    nome: str


class PublisherCreate(PublisherBase):
    pass


class Publisher(PublisherBase):
    id: int

    class ConfigDict:
        from_attributes = True


class PublisherItems(BaseModel):
    items: list[Publisher]
