import http

from flask_restx import Resource, Namespace, fields

from app.services.disc_service import DiscService
from app.services.artist_service import ArtistService
from app.service.artist_disc_service import ArtistDiscService
from app.services.rented_service import RentedService



# Namespaces
discs_namespace = Namespace(name="Disc")
artists_namespace = Namespace(name="Artist")
artists_discs_namespace = Namespace(name="ArtistDisc")
rented_namespace = Namespace(name="Rented")

# Models
# Disc Models
disc_model = discs_namespace.model('disc', {
    'id': fields.Integer(readOnly=True),
    'title': fields.String(required=True),
    'year': fields.String(required=True),
    'description': fields.String(required=True),
    'artist_id': fields.String(readOnly=True),
    'artists': fields.String(required=True),
    'rented': fields.Boolean(),
})
disc_create_model = discs_namespace.model('disc_create', {
    'id': fields.Integer(readOnly=True),
    'title': fields.String(required=True),
    'year': fields.String(required=True),
    'description': fields.String(required=True),
    'artist_id': fields.String(readOnly=True),
    'artists': fields.String(required=True),
    'rented': fields.Boolean(),
})
disc_update_model = discs_namespace.model('disc_update', {
    'id': fields.Integer(readOnly=True),
    'title': fields.String(),
    'year': fields.String(),
    'description': fields.String(),
    'artist_id': fields.String(readOnly=True),
    'artists': fields.String(),
    'rented': fields.Boolean(),
})

#Artist Models

artist_model = artists_namespace.model('artist', {
    'id': fields.Integer(readOnly=True),
    'artist': fields.Integer(required=True),
    'about': fields.String(required=True),
    'disc_artist': fields.String(required=True),
    'disc_a_d': fields.String(required=True)
    
})
artist_create_model = artists_namespace.model('artist_create', {
    'id': fields.Integer(readOnly=True),
    'artist': fields.Integer(required=True),
    'about': fields.String(required=True),
    'disc_artist': fields.String(required=True),
    'disc_a_d': fields.String(required=True)

})
artist_update_model = artists_namespace.model('artist_update', {
    'id': fields.Integer(readOnly=True),
    'artist': fields.Integer(required=True),
    'about': fields.String(required=True),
    'disc_artist': fields.String(required=True),
    'disc_a_d': fields.String(required=True)

})

# ArtistDisc Models

artist_disc_model = artists_namespace.model('artist_disc', {
    'id': fields.Integer(readOnly=True),
    'artist_id': fields.Integer(required=True),
    'disc_id': fields.String(required=True)
    
})
artist_disc_create_model = artists_namespace.model('artist_disc_create', {
    'id': fields.Integer(readOnly=True),
    'artist_id': fields.Integer(required=True),
    'disc_id': fields.String(required=True)

})
artist_disc_update_model = artists_namespace.model('artist_disc_update', {
    'id': fields.Integer(readOnly=True),
    'artist_id': fields.Integer(required=True),
    'disc_id': fields.String(required=True)

})

# Rented Models

rented_model = rented_namespace.model('rented', {
    'id': fields.Integer(readOnly=True),
    'date': fields.Integer(required=True),
    'disc_id': fields.String(required=True)
    
})
rented_create_model = rented_namespace.model('rented_create', {
    'id': fields.Integer(readOnly=True),
    'date': fields.Integer(required=True),
    'disc_id': fields.String(required=True)

})
rented_update_model = rented_namespace.model('rented_update', {
    'id': fields.Integer(readOnly=True),
    'date': fields.Integer(required=True),
    'disc_id': fields.String(required=True)

})

@discs_namespace.route('/')
class DiscAPI(Resource):

    @discs_namespace.marshal_list_with(disc_model)
    def get(self):
        return DiscService().get_all()

    @discs_namespace.expect(disc_create_model)
    @discs_namespace.response(201, "Disc created")
    def post(self):
        new_disc = DiscService().create(**discs_namespace.payload)
        
        if new_disc:
            return "OK", 201
        return discs_namespace.abort(500)

@discs_namespace.route('/<int:disc>')

class ArtistDiscAPI(Resource):

    @discs_namespace.marshal_with(disc_model)
    def get(self, disc: int):
        return ArtistDiscService().get_by_id(disc)

    @discs_namespace.expect(disc_update_model)
    @discs_namespace.marshal_with(disc_model)
    def put(self, disc: int):
        return ArtistDiscService().update(disc, **discs_namespace.payload)

    @discs_namespace.response(200, "OK")
    def delete(self, disc: int):
        ArtistDiscService().delete(disc)
        return "OK", 200

@artists_namespace.route('/<int:artist>')
class ArtistAPI(Resource):

    @artists_namespace.marshal_with(artist_model)
    def get(self, artist: int):
        return ArtistService().get_by_id(artist)

    @artists_namespace.expect(artist_update_model)
    @artists_namespace.marshal_with(artist_model)
    def put(self, artist: int):
        return ArtistService().update(artist, **artists_namespace.payload)

    @artists_namespace.response(200, "OK")
    def delete(self, artist: int):
        ArtistService().delete(artist)
        return "OK", 200



@rented_namespace.route('/<int:rented>')
class RentedAPI(Resource):

    @rented_namespace.marshal_with(rented_model)
    def get(self, rented: int):
        return RentedService().get_by_id(rented)

    @rented_namespace.expect(rented_update_model)
    @rented_namespace.marshal_with(rented_model)
    def put(self, rented: int):
        return RentedService().update(rented, **rented_namespace.payload)

    @rented_namespace.response(200, "OK")
    def delete(self, rented: int):
        RentedService().delete(rented)
        return "OK", 200