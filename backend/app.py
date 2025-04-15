from flask import Flask, request, jsonify
from config import Config
#from sighting import Sighting
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)


class Sighting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Sighting {self.animal_name} at {self.latitude}, {self.longitude}>'


@app.route('/upload', methods=['POST'])
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

@app.route('/sightings', methods=['GET'])
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

@app.route('/sightings/<int:id>', methods=['GET'])
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

@app.route('/sightings/int:id>', methods=['DELETE'])
def delete_sighting_by_id(id):
    sighting = Sighting.query.get(id)

    if not sighting:
        return jsonify({"message": "sighting not found"}), 404

    db.session.delete(sighting)
    db.session.commit()

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)