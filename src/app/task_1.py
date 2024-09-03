import json
from pprint import pprint

from app.parsers.detmir_parser import DetmirParser
from app.scripts.save_detmir_to_db import save_detmir_to_db

if __name__ == "__main__":
    detmir_parser = DetmirParser()
    res = detmir_parser.get_detmir_data()
    json.dumps(res, indent=4)
    save_detmir_to_db(res)
    pprint(res)
