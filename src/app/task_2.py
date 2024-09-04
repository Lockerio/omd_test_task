import json
from pprint import pprint

import requests

from app.database.container import product_service
from app.parsers.perecrestok_parser import PerecrestokParser
from app.scripts.format_perecrestok_data import format_perecrestok_data


if __name__ == "__main__":
    url = "https://www.perekrestok.ru/api/customer/1.4.1.0/catalog/product/plu4318836"

    perecrestok_parser = PerecrestokParser()
    src_res = perecrestok_parser.get_product_data(url)
    res = format_perecrestok_data(src_res)

    product_service.create(res)
    with open("data2.json", "w", encoding="utf-8") as json_file:
        json.dump(res, json_file, ensure_ascii=False, indent=4)
