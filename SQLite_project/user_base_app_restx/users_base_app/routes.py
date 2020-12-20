import http

from flask_restx import Resource, Namespace, fields

from users_base_app.service import UserService

# Namespaces
users_namespace = Namespace(name="Users")

# Models
user_model = users_namespace.model('user', {
    'id': fields.Integer(readOnly=True),
    'name': fields.String(required=True),
})
user_create_model = users_namespace.model('user_create', {
    'name': fields.String(required=True),
    'password': fields.String(required=True)
})
user_update_model = users_namespace.model('user_update', {
    'name': fields.String(required=True),
    'password': fields.String()
})


@users_namespace.route('/')
class UsersAPI(Resource):

    @users_namespace.marshal_list_with(user_model)
    def get(self):
        return UserService().get_all()

    @users_namespace.expect(user_create_model)
    @users_namespace.response(201, "User created")
    def post(self):
        new_user = UserService().create(**users_namespace.payload)
        if new_user:
            return "OK", 201
        return users_namespace.abort(500)


@users_namespace.route('/<int:user>')
class SelectedUserAPI(Resource):

    @users_namespace.marshal_with(user_model)
    def get(self, user: int):
        return UserService().get_by_id(user)

    @users_namespace.expect(user_update_model)
    @users_namespace.marshal_with(user_model)
    def put(self, user: int):
        return UserService().update(user, **users_namespace.payload)

    @users_namespace.response(200, "OK")
    def delete(self, user: int):
        UserService().delete(user)
        return "OK", 200
