from sqlalchemy.orm import Session

from app.database.dals.detmir_dal import DetmirDAO
from app.database.dals.product_dal import ProductDAO
from app.database.db import engine
from app.database.services.detmir_service import DetmirService
from app.database.services.product_service import ProductService

session = Session(bind=engine)


detmir_dao = DetmirDAO(session)
product_dao = ProductDAO(session)

detmir_service = DetmirService(detmir_dao)
product_service = ProductService(product_dao)
