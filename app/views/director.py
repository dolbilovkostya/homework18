from flask_restx import Namespace, Resource

from implemented import director_service, directors_schema, director_schema

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get_one(self, did: int):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200
