from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from livraria.auth import crud, schemas, utils
from livraria.database import get_db

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post("/signup")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    token = utils.create_token(user, db)
    return token


@router.post("/login")
def login(token=Depends(utils.create_token)):
    return token
