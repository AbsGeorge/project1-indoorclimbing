from application import db

class climbing_centre(db.Model):
    centre_id = db.Column(db.integer, primary_key=True)
    centre_name = db.Column(db.string(50), nullable=False)
    average_ratings = db.Column(db.int, nullable=False)
    address = db.Column(db.string(100), )
