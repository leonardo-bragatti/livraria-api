from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from livraria.auth import utils
from livraria.categories import crud, schemas
from livraria.database import get_db

router = APIRouter(
    prefix="/categorias",
    tags=["categorias"],
    dependencies=[Depends(utils.verify_token)],
)


@router.post("", response_model=schemas.Category, status_code=HTTPStatus.CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.create_category(db, category)
    return db_category


@router.get("", response_model=schemas.CategoryItems)
def get_categories(db: Session = Depends(get_db)):
    return {"items": crud.get_categories(db)}


@router.get("/{category_id}", response_model=schemas.Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id)
    if not db_category:
        raise HTTPException(
            HTTPStatus.NOT_FOUND,
        )
    return db_category


@router.put("/{category_id}", response_model=schemas.Category)
def update_category(
    category_id: int, category: schemas.CategoryCreate, db: Session = Depends(get_db)
):
    db_category = crud.update_category(db, category_id, category)
    if not db_category:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Category not found")
    return db_category


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.delete_category(db, category_id)
    if not db_category:
        raise HTTPException(HTTPStatus.NOT_FOUND, "Category not found")
