from flask import request
from flask_restx import Namespace, Resource

from implemented import movie_service, movies_schema, movie_schema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')

        data = {
            'director_id': request.args.get('director_id'),
            'genre_id': request.args.get('genre_id'),
            'year': request.args.get('year')
        }

        all_movies = movie_service.filter(data)

        return movies_schema.dump(all_movies)


    def post(self):
        data = request.json
        new_movie = movie_service.add_movie(data)
        return '', 201, {'location': f'/movies/{new_movie}'}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid: int):
        data = request.json
        data['id'] = mid
        movie_service.update(data)

        return 'Movie updated', 201

    def delete(self, mid: int):
        movie_service.delete_movie(mid)
        return 'Movie deleted', 202
