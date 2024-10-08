from typing import Any

from app.database.models import DetMir


class DetmirDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, detmir_id: int) -> DetMir:
        return self.session.query(DetMir).get(detmir_id)

    def get_all(self) -> list[DetMir]:
        return self.session.query(DetMir).all()

    def create(self, data: dict[str, Any]) -> None:
        detmir = DetMir(**data)
        self.session.add(detmir)
        self.session.commit()

    def delete(self, detmir_id: int) -> None:
        detmir = self.get_one(detmir_id)
        self.session.delete(detmir)
        self.session.commit()
