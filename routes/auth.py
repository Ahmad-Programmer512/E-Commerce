# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from database import schema, database, models
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm    

# router = APIRouter()

# @router.get("/auth")
# def auth(user_data: OAuth2PasswordRequestForm, db: Session = Depends(database.get_db)):
#     user = db.query(models.User).filter(models.User.email == user_data.username).first()

#     if user is None: