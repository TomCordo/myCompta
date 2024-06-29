from sqlalchemy.orm import Session
from . import models, schemas
from .hashing import Hash


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def verify_password(plain_password: str, hashed_password: str):
    return Hash.verify(hashed_password, plain_password)


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
