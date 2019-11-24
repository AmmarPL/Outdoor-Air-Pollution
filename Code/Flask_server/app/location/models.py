from flask_sqlalchemy import SQLAlchemy
from app import db


class Location(db.Model):
    """

        Table storing the location

    """
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.String, unique=False)
    lon = db.Column(db.String, unique=False)

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def to_string(self):

        return self.lat + ',' + self.lon
