
from app.models import Disc
import db


class DiscService:
    model = Disc  # type: db.Model

    def __init__(self):
        if self.model is None:
            raise NotImplementedError("Model Class is not defined")

    def get_by_id(self, id: int):
        return self.model.query.get(id)

    def get_all(self):
        return self.model.query.all()

    def create(self, **kwargs):
        new_object = self.model(**kwargs)
        db.session.add(new_object)
        db.session.commit()
        return new_object

    def update(self, id: int, **kwargs):
        selected_object = self.get_by_id(id)
        if selected_object:
            for key, value in kwargs.items():
                setattr(selected_object, key, value)
            db.session.commit()
        return selected_object

    def delete(self, id: int):
        selected_object = self.get_by_id(id)
        if selected_object:
            db.session.delete(selected_object)

