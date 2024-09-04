from sqlalchemy import inspect

from app.database.container import detmir_service, product_service

detmir_collection = detmir_service.get_all()
for element in detmir_collection:
    inspector = inspect(element)
    attributes = {c.key: getattr(element, c.key) for c in inspector.mapper.column_attrs}
    print(attributes)

product_collection = product_service.get_all()
for element in product_collection:
    inspector = inspect(element)
    attributes = {c.key: getattr(element, c.key) for c in inspector.mapper.column_attrs}
    print(attributes)
