# Main app
# main.py

from fastapi import FastAPI
from . import models
from .routers import users
from .database import engine, get_db

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Modular FastAPI application!"}
