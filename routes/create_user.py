from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import models, schema, database
from Token.hashing import hash

router = APIRouter()

@router.post("/create_user")
def create_user(user: schema.User, db: Session = Depends(database.get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    user.password = hash(user.password)

    new_user = models.User(**user.model_dump())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "Sign up successfuly"}