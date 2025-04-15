from flask import Blueprint

sightings_bp = Blueprint('sightings', __name__)

from . import routes