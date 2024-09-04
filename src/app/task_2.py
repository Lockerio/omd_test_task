import json

from app.database.container import product_service
from app.parsers.perecrestok_parser import PerecrestokParser
from app.utils.perecrestok_formatter import PerecrestokFormatter

if __name__ == "__main__":
    url = "https://www.perekrestok.ru/api/customer/1.4.1.0/catalog/product/plu4318836"

    perecrestok_parser = PerecrestokParser()
    src_res = perecrestok_parser.get_product_data(url)
    print(src_res)
    json_res = PerecrestokFormatter.src_json_to_output_json(src_res)
    db_json_res = PerecrestokFormatter.json_to_db_json(json_res)

    product_service.create(db_json_res)
    with open("Product.json", "w", encoding="utf-8") as json_file:
        json.dump(json_res, json_file, ensure_ascii=False, indent=4)
