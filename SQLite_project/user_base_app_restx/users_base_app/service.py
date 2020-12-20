import hashlib
import uuid

from users_base_app.models import User
from users_base_app import db


class Service:
    model = None  # type: db.Model

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


class UserService(Service):
    model = User

    def create(self, name: str, password: str):
        salt = self.generate_salt()
        password = self.hash_password(password, salt)
        return super().create(name=name, password=password, salt=salt)

    def update(self, id: int, **kwargs):
        if 'salt' in kwargs:
            raise PermissionError("Cannot update salt manually")
        if 'password' in kwargs:
            password = kwargs['password']
            new_salt = self.generate_salt()
            new_password = self.hash_password(password, new_salt)
            kwargs['salt'] = new_salt
            kwargs['password'] = new_password
        return super().update(id, **kwargs)

    @staticmethod
    def hash_password(password: str, salt: str):
        hash = hashlib.sha256()
        hash.update((salt + password).encode())
        return hash.hexdigest()

    @staticmethod
    def generate_salt():
        return str(uuid.uuid4()).replace('-', '')
