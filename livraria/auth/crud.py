from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import Session

from livraria.auth import schemas
from livraria.database import models


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pbkdf2_sha256.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return db_user
