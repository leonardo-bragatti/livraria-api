from sqlalchemy import Column, ForeignKey, Integer, String

from livraria.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, index=True)
    hashed_password = Column(String)


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    nome = Column(String)


class Publisher(Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True)
    nome = Column(String)


class Author(Base):
    __tablename__ = "tb_author"

    id = Column(Integer, primary_key=True)
    nome = Column(String)


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)

    titulo = Column(String)
    capa = Column(String)
    isbn = Column(String)
    paginas = Column(Integer)
    ano = Column(Integer)

    publisher_id = Column(Integer, ForeignKey("publisher.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    author_id = Column(Integer, ForeignKey("author.id"))
