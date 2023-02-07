from marshmallow import Schema, fields
from setup_db import db


class Genre(db.Model):
    __tablename__ = 'Genre'

    id = db.Column(db.Integer, primaty_key=True)
    name = db.Column(db.String(250))


class GenreSchema(Schema):
    id = fields.Integer()
    name = fields.String()
