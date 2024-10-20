from sqlalchemy.orm import Session

from livraria.database import models
from livraria.publishers import schemas


def create_publisher(db: Session, publisher: schemas.PublisherCreate):
    db_publisher = models.Publisher(**publisher.model_dump())
    db.add(db_publisher)
    db.commit()
    return db_publisher


def get_publishers(db: Session) -> list[models.Publisher]:
    return db.query(models.Publisher).all()


def get_publisher(db: Session, publisher_id: int) -> models.Publisher:
    return (
        db.query(models.Publisher).filter(models.Publisher.id == publisher_id).first()
    )


def update_publisher(
    db: Session, publisher_id: int, publisher: schemas.PublisherCreate
) -> models.Publisher | None:
    db_publisher = get_publisher(db, publisher_id)
    if not db_publisher:
        return

    db_publisher.nome = publisher.nome
    db.add(db_publisher)
    db.commit()
    return db_publisher


def delete_publisher(db: Session, publisher_id: int) -> models.Publisher | None:
    db_publisher = get_publisher(db, publisher_id)
    if not db_publisher:
        return

    db.delete(db_publisher)
    db.commit()
    return db_publisher
