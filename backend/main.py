from flask import Flask, jsonify
from extensions import db, jwt
from auth import auth_bp
from users import user_bp
from sightings import sighting_bp
from models import User

def create_app():

    app = Flask(__name__)

    app.config.from_prefixed_env()

    # initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # register blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(sighting_bp, url_prefix="/sightings")

    # load user
    @jwt.user_lookup_loader
    def user_lookup_callback(__jwt__headers, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(username = identity).one_or_none()

    # additional claims
    @jwt.additional_claims_loader
    def make_additional_claims(identity):
        if identity == "joe123":
            return {"is_staff": True}
        return {"is_staff": False}

    # jwt error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message": "Token has expired", "error": "token_expired"}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({"message": "Signaure verification failed", "error": "invalid_token"}), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({"message": "Request does not contain a valid token", "error": "authorization_header"}),401



    return app