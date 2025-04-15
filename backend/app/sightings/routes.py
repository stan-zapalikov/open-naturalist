from flask import request, jsonify
from app.models import Sighting
from app import db
from . import sightings_bp

@sightings_bp.route('/upload', methods=['POST'])
def create_sighting():
    data = request.json
    name = data.get('animal_name')
    lat = data.get('latitude')
    lon = data.get('longitude')

    if not name or lat is None or lon is None:
        return jsonify({'error': 'missing fields'}), 400

    new_sighting = Sighting(animal_name=name, latitude=lat, longitude=lon)
    db.session.add(new_sighting)
    db.session.commit()
    return jsonify({'message': 'Sighting saved'}), 201

@sightings_bp.route('/sightings', methods=['GET'])
def get_sightings():
    sightings = Sighting.query.all()
    return jsonify([
        {
            'id': s.id,
            'animal_name': s.animal_name,
            'latitude': s.latitude,
            'longitude': s.longitude
        }
        for s in sightings
    ])

@sightings_bp.route('/sightings/<int:id>', methods=['GET'])
def get_sighting_by_id(id):
    sighting = Sighting.query.get(id)

    if not sighting:
        return jsonify({"message": "sighting not found"}), 404

    return jsonify(
        {
            'id': sighting.id,
            'animal_name': sighting.animal_name,
            'latitude': sighting.latitude,
            'longitude': sighting.longitude
        }
    )

@sightings_bp.route('/sightings/<int:id>', methods=['DELETE'])
def delete_sighting_by_id(id):
    sighting = Sighting.query.get(id)

    if not sighting:
        return jsonify({"message": "sighting not found"}), 404

    db.session.delete(sighting)
    db.session.commit()