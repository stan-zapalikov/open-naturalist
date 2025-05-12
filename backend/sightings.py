from flask import Blueprint, jsonify, request
from flask_jwt_extended import (create_access_token, 
                                create_refresh_token, 
                                jwt_required, 
                                get_jwt, 
                                current_user,
                                get_jwt_identity)
from schemas import SightingSchema
from models import Sighting

sighting_bp = Blueprint("sightings", __name__)

@sighting_bp.get("/all")
def get_all_sightings():
    
    name = request.args.get("name")
    latitude = request.args.get("latitude")
    longitude = request.args.get("longitude")

    sightings = Sighting.query.paginate(
        name = name,
        latitude = latitude,
        longitude = longitude
    )

    return jsonify({"sightings": SightingSchema().dump})