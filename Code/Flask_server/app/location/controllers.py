from flask import Blueprint, request, session, jsonify
from app import db
from .models import Location

mod_loc = Blueprint('location', __name__, url_prefix='/loc')


@mod_loc.route('/add', methods=['POST'])
def add_loc():

    lat = request.form['lat']
    lon = request.form['lon']

    new_loc = Location(lat, lon)
    db.session.add(new_loc)
    db.session.commit()

    return jsonify(success=True, location=new_loc.to_string())


@mod_loc.route('/', methods=['GET'])
def get_loc():

    loc = Location.query.filter_by(id=1).first()

    return jsonify(success=True, location=loc.to_string())


@mod_loc.route('/all', methods=['GET'])
def get_all():

    loc = Location.query.all()

    return jsonify(success=True, locations=[locs.to_string() for locs in loc])


@mod_loc.route('/del', methods=['GET'])
def del_loc():

    id_to_del = request.args.get('id')
    loc = Location.query.filter_by(id=id_to_del).first()
    db.session.delete(loc)
    db.session.commit()

    return jsonify(success=True, location=loc.to_string())


@mod_loc.route('/upd', methods=['POST'])
def upd_loc():

    lat = request.form['lat']
    lon = request.form['lon']
    loc = Location.query.filter_by(id=1).first()
    loc.lat = lat
    loc.lon = lon
    db.session.commit()

    return jsonify(success=True, location=loc.to_string())
