import json

from app.database.container import detmir_service
from app.parsers.detmir_parser import DetmirParser


if __name__ == "__main__":
    detmir_parser = DetmirParser()
    res = detmir_parser.get_detmir_data()

    for element in res:
        detmir_service.create(element)
    with open("DetMir.json", "w", encoding="utf-8") as json_file:
        json.dump(res, json_file, ensure_ascii=False, indent=4)
