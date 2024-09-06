from typing import Any

from app.database.dals.product_dal import ProductDAO
from app.database.models import Product


class ProductService:
    def __init__(self, dao: ProductDAO):
        self.dao = dao

    def get_one(self, product_id) -> Product:
        return self.dao.get_one(product_id)

    def get_all(self) -> list[Product]:
        return self.dao.get_all()

    def create(self, data: dict[str, Any]) -> None:
        self.dao.create(data)

    def delete(self, product_id: int) -> None:
        self.dao.delete(product_id)
