from sqlalchemy.orm import Session

from livraria.categories import schemas
from livraria.database import models


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    return db_category


def get_categories(db: Session) -> list[models.Category]:
    return db.query(models.Category).all()


def get_category(db: Session, category_id: int) -> models.Category:
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def update_category(
    db: Session, category_id: int, category: schemas.CategoryCreate
) -> models.Category | None:
    db_category = get_category(db, category_id)
    if not db_category:
        return

    db_category.nome = category.nome
    db.add(db_category)
    db.commit()
    return db_category


def delete_category(db: Session, category_id: int) -> models.Category | None:
    db_category = get_category(db, category_id)
    if not db_category:
        return

    db.delete(db_category)
    db.commit()
    return db_category
