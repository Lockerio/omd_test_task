from app.database.dals.product_dal import ProductDAO


class ProductService:
    def __init__(self, dao: ProductDAO):
        self.dao = dao

    def get_one(self, product_id):
        return self.dao.get_one(product_id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        self.dao.create(data)

    def delete(self, product_id):
        self.dao.delete(product_id)
