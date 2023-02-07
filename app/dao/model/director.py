from marshmallow import Schema, fields
from setup_db import db


class Director(db.Model):
    __tablename__ = 'Director'

    id = db.Column(db.Integer, primaty_key=True)
    name = db.Column(db.String(250))


class DirectorSchema(Schema):
    id = fields.Integer()
    name = fields.String()

