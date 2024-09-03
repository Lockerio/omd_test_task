from sqlalchemy import Column, Integer, String, Float

from app.database.db import Base


class DetMir(Base):
    __tablename__ = 'DetMir'

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    image_url = Column(String(), nullable=False)
    content_url = Column(String(), nullable=False)
    meta = Column(String(), nullable=False)
    place = Column(Integer(), nullable=False)
    position = Column(Integer(), nullable=False)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(), nullable=False)
    price = Column(Float(), nullable=False)
    price_sale = Column(Float(), nullable=False)
    description = Column(String(), nullable=False)
    code = Column(String(), nullable=False)
    images = Column(String(), nullable=False)
    comment_count = Column(Integer(), nullable=False)
    rating = Column(Float(), nullable=False)
    brand = Column(String(), nullable=False)
    categories = Column(String(), nullable=False)
    content_url = Column(String(), nullable=False)
