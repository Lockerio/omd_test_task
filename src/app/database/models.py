from sqlalchemy import Column, Integer, String, Float

from app.database.db import Base


class DetMir(Base):
    __tablename__ = 'DetMir'

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    image_url = Column(String(), nullable=False)
    content_url = Column(String(), nullable=False)
    meta = Column(String())
    place = Column(Integer(), nullable=False)
    position = Column(Integer(), nullable=False)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    name = Column(String())
    price = Column(Float())
    price_sale = Column(Float())
    description = Column(String())
    code = Column(String())
    images = Column(String())
    comment_count = Column(Integer())
    rating = Column(Float())
    brand = Column(String())
    categories = Column(String())
    content_url = Column(String())
