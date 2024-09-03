from app.database.models import Product


class ProductDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, product_id):
        return self.session.query(Product).get(product_id)

    def get_all(self):
        return self.session.query(Product).all()

    def create(self, data):
        product = Product(**data)
        self.session.add(product)
        self.session.commit()

    def delete(self, product_id):
        product = self.get_one(product_id)
        self.session.delete(product)
        self.session.commit()
