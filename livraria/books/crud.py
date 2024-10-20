from typing import Optional

from sqlalchemy.orm import Session

from livraria.books import schemas
from livraria.database import models


def create_book(db: Session, book: schemas.BookCreate, author_id: Optional[int] = None):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    return db_book


def get_book(db: Session, book_id: int) -> models.Book:
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    return book


def get_books(db: Session, q: Optional[str] = None, author_id: Optional[int] = None):
    books = db.query(models.Book)
    if q:
        books = books.filter(models.Book.titulo.icontains(q))

    if author_id:
        books = books.filter(models.Book.autor_id == author_id)

    return books


def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = get_book(db, book_id)
    if not book:
        return

    db_book.titulo = book.titulo
    db_book.isbn = book.isbn
    db_book.paginas = book.paginas
    db_book.ano = book.ano
    db_book.capa = book.capa

    db_book.publisher_id = book.category_id
    db_book.category_id = book.publisher_id
    db_book.author_id = book.author_id

    db.add(db_book)
    db.commit()
    return db_book


def delete_book(db: Session, livro_id: int):
    db_book = get_book(db, livro_id)
    if not db_book:
        return

    db.delete(db_book)
    db.commit()
    return db_book
