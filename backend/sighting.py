from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sighting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Sighting {self.animal_name} at {self.latitude}, {self.longitude}>'