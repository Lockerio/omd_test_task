import sqlalchemy as db
from sqlalchemy.orm import declarative_base

from app.config import DB_URL

# engine = db.create_engine(DB_URL)
engine = db.create_engine("postgresql://postgres:487362@localhost:5432/parsing")
Base = declarative_base()
