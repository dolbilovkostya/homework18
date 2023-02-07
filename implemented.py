from app.dao.movie_dao import MovieDao
from app.dao.genre_dao import GenreDao
from app.dao.director_dao import DirectorDao

from app.service.movie_service import MovieService
from app.service.genre_service import GenreService
from app.service.director_service import DirectorService

from app.dao.model.movie import MovieSchema
from app.dao.model.genre import GenreSchema
from app.dao.model.director import DirectorSchema

from setup_db import db

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
