from sqlalchemy.orm import backref
from application import db

class ClimbingCentre(db.Model):
    centre_id = db.Column(db.Integer, primary_key=True)
    centre_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100))
    climbers = db.relationship("ClimberInformation", backref="centre")

class ClimberInformation(db.Model):
    climber_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100))
    centre_id = db.Column(db.Integer, db.ForeignKey("climbing_centre.centre_id"))