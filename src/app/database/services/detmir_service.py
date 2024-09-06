from typing import Any

from app.database.dals.detmir_dal import DetmirDAO
from app.database.models import DetMir


class DetmirService:
    def __init__(self, dao: DetmirDAO):
        self.dao = dao

    def get_one(self, detmir_id: int) -> DetMir:
        return self.dao.get_one(detmir_id)

    def get_all(self) -> list[DetMir]:
        return self.dao.get_all()

    def create(self, data: dict[str, Any]) -> None:
        self.dao.create(data)

    def delete(self, detmir_id: int) -> None:
        self.dao.delete(detmir_id)
