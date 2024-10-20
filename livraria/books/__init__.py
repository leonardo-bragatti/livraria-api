from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from livraria.auth.utils import verify_token
from livraria.books import crud, schemas
from livraria.database import get_db

router = APIRouter(
    prefix="/livros", tags=["livros"], dependencies=[Depends(verify_token)]
)


@router.post("", response_model=schemas.Book, status_code=HTTPStatus.CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.create_book(db, book)
    return db_book


@router.get("", response_model=schemas.BookItems)
def get_books(q: str = "", limit: int = 100, db: Session = Depends(get_db)):
    db_books = crud.get_books(db, q, limit)
    return {"items": db_books}


@router.get("/{livro_id}", response_model=schemas.Book)
def get_book(livro_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, livro_id)
    if not db_book:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Book not found")

    return db_book


@router.put("/{livro_id}", response_model=schemas.Book)
def update_book(livro_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, livro_id, book)
    if not db_book:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Book not found")

    return db_book


@router.delete("/{livro_id}")
def delete_book(livro_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, livro_id)
    if not db_book:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Book not found")
