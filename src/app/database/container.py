from sqlalchemy.orm import Session

from app.database.db import engine

session = Session(bind=engine)