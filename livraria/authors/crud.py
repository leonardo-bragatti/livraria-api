from sqlalchemy.orm import Session

from livraria.authors import schemas
from livraria.database import models


def create_author(db: Session, author: schemas.AuthorCreate) -> models.Author:
    db_author = models.Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    return db_author


def get_authors(db: Session) -> list[models.Author]:
    return db.query(models.Author).all()


def get_author(db: Session, book_id: int) -> models.Author:
    db_author = db.query(models.Author).filter(models.Book.id == book_id).first()
    return db_author


def update_author(
    db: Session, author_id: int, author: schemas.AuthorCreate
) -> models.Author | None:
    db_author = get_author(db, author_id)
    if not db_author:
        return

    db_author.nome = author.nome
    db.add(db_author)
    db.commit()
    return db_author


def delete_author(db: Session, author_id: int):
    db_author = get_author(db, author_id)
    if not db_author:
        return

    db.delete(db_author)
    db.commit()
    return db_author
