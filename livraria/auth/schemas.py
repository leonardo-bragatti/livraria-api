from pydantic import BaseModel, Field


class EmailAuthentication(BaseModel):
    email: str
    password: str = Field(alias="senha")


class UserCreate(EmailAuthentication):
    password_validation: str = Field(alias="confirmarSenha")
