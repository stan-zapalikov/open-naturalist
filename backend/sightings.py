from flask import Blueprint, jsonify, request
from flask_jwt_extended import (create_access_token, 
                                create_refresh_token, 
                                jwt_required, 
                                get_jwt, 
                                current_user,
                                get_jwt_identity)
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from schemas import SightingSchema
from models import Sighting

sighting_bp = Blueprint("sightings", __name__)

@sighting_bp.get("/all")
def get_all_sightings():
    
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    sightings = Sighting.query.paginate(
        page = page,
        per_page=per_page
    )

    return jsonify({"sightings": SightingSchema().dump(sightings, many=True)})

@sighting_bp.post("/upload")
@jwt_required()
def upload_sighting():
    data = request.get_json()

    sighting = Sighting.get_sighting_by_details(
        name= data.get("name"),
        location = Point(data.get("longitude"), data.get("latitude"), srid=4326)
    )

    if sighting is None:
        return jsonify({"error": "sighting already exists"}), 409

    new_sighting = Sighting(
        name= data.get("name"),
        location = Point(data.get("longitude"), data.get("latitude"), srid=4326)
    )

    new_sighting.save()

    return jsonify({"message": "sighting created"}), 201



