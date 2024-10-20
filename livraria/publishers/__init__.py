from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from livraria.auth import utils
from livraria.database import get_db
from livraria.publishers import crud, schemas

router = APIRouter(
    prefix="/editoras", tags=["editoras"], dependencies=[Depends(utils.verify_token)]
)


@router.post("", response_model=schemas.Publisher, status_code=HTTPStatus.CREATED)
def create_publisher(publisher: schemas.PublisherCreate, db: Session = Depends(get_db)):
    db_category = crud.create_publisher(db, publisher)
    return db_category


@router.get("", response_model=schemas.PublisherItems)
def get_publishers(db: Session = Depends(get_db)):
    return {"items": crud.get_publishers(db)}


@router.get("/{publisher_id}", response_model=schemas.Publisher)
def get_publisher(publisher_id: int, db: Session = Depends(get_db)):
    db_publisher = crud.get_publisher(db, publisher_id)
    if not db_publisher:
        raise HTTPException(
            HTTPStatus.NOT_FOUND,
        )
    return db_publisher


@router.put("/{publisher_id}", response_model=schemas.Publisher)
def update_publisher(
    publisher_id: int, publisher: schemas.PublisherCreate, db: Session = Depends(get_db)
):
    db_publisher = crud.update_publisher(db, publisher_id, publisher)
    if not db_publisher:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Publisher not found")
    return db_publisher


@router.delete("/{publisher_id}")
def delete_publisher(publisher_id: int, db: Session = Depends(get_db)):
    db_publisher = crud.delete_publisher(db, publisher_id)
    if not db_publisher:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Publisher not found")
