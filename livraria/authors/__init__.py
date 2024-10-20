from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from livraria.auth import utils
from livraria.authors import crud, schemas
from livraria.database import get_db

router = APIRouter(
    prefix="/autores", tags=["autores"], dependencies=[Depends(utils.verify_token)]
)


@router.post("", response_model=schemas.Author, status_code=HTTPStatus.CREATED)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_category = crud.create_author(db, author)
    return db_category


@router.get("", response_model=schemas.AuthorItems)
def get_authors(db: Session = Depends(get_db)):
    return {"items": crud.get_authors(db)}


@router.get("/{author_id}", response_model=schemas.Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id)
    if not db_author:
        raise HTTPException(
            HTTPStatus.NOT_FOUND,
        )
    return db_author


@router.put("/{author_id}", response_model=schemas.Author)
def update_author(
    author_id: int, author: schemas.AuthorCreate, db: Session = Depends(get_db)
):
    db_author = crud.update_author(db, author_id, author)
    if not db_author:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Author not found")
    return db_author


@router.delete("/{author_id}")
def delete_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.delete_author(db, author_id)
    if not db_author:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Author not found")
