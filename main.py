from fastapi import FastAPI
from routes import auth, create_user
from database.database import Base, engine
from database import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "E-Commerce"}

# app.include_router(auth.router)
app.include_router(create_user.router)