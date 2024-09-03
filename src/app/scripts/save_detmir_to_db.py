from typing import Any

from app.database.container import detmir_service


def save_detmir_to_db(data: list[dict[str, Any]]):
    for element in data:
        detmir_service.create(element)
