from app.database.dals.detmir_dal import DetmirDAO


class DetmirService:
    def __init__(self, dao: DetmirDAO):
        self.dao = dao

    def get_one(self, detmir_id):
        return self.dao.get_one(detmir_id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        self.dao.create(data)

    def delete(self, detmir_id):
        self.dao.delete(detmir_id)
