import time
from datetime import UTC, datetime, timedelta
from http import HTTPStatus

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import Session

from livraria.auth import crud, schemas
from livraria.database import get_db

SECRET = "my_secret"
ALGORITHM = "HS256"

authentication_bearer = HTTPBearer()


def authenticate_user(db: Session, email: str, password: str):
    db_user = crud.get_user_by_email(db, email)
    if not db_user:
        return

    if not pbkdf2_sha256.verify(password, db_user.hashed_password):
        return

    return db_user


def create_token(
    credentials: schemas.EmailAuthentication, db: Session = Depends(get_db)
):
    user = authenticate_user(db, credentials.email, credentials.password)
    if not user:
        raise HTTPException(HTTPStatus.UNAUTHORIZED, "Invalid user or password")

    expiration_date = datetime.now(UTC) + timedelta(minutes=15)
    token = jwt.encode({"email": user.email, "exp": expiration_date}, SECRET, ALGORITHM)
    unix_time = time.mktime(expiration_date.timetuple())

    return {"token": token, "exp": unix_time}


def verify_token(
    token: HTTPAuthorizationCredentials = Depends(authentication_bearer),
    db: Session = Depends(get_db),
):
    try:
        data = jwt.decode(token.credentials, SECRET, algorithms=ALGORITHM)
    except jwt.exceptions.DecodeError:
        raise HTTPException(HTTPStatus.BAD_REQUEST, "Invalid token")
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(HTTPStatus.BAD_REQUEST, "Token expired")

    email = data.get("email")
    user = crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(HTTPStatus.UNAUTHORIZED, "Invalid credentials")

    return user
