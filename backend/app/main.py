from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from passlib.context import CryptContext

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create user route
@app.post("/users/", response_model=schemas.UserResponseModel)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(user.password)
    user_with_hashed_password = schemas.UserCreate(
        email=user.email, password=hashed_password
    )
    return crud.create_user(db=db, user=user_with_hashed_password)


# Login route
@app.post("/login/")
def login(user_login: schemas.UserLogin, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, user_login.email)
    if user is None or not crud.verify_password(
        user_login.password, user.hashed_password
    ):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return {"message": "Login successful"}
