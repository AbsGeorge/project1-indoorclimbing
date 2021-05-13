from application import app, db 
from application.models import climbing_centre

@app.route("/")
@app.route("/home")
def home():
    all_centre = climbing_centre.query.all()
    return str(all_centre)

@app.route("/create")
def create():
    new_centre_name = climbing_centre(centre_name = "What is the name of the Climbing Centre you visited")
    db.session.add(new_centre_name)
    db.session.commit()
    new_centre_rating = climbing_centre(average_ratings = "How difficult will you rate your climb?")
    db.session.add(new_centre_rating)
    db.session.commit()
    return new_centre_name + new_centre_rating

@app.route("/update/<int:id>")
def update(id):
    centre_change = climbing_centre.query.filter_by(id=id)
    new_centre = redirect (url("create"))
    db.session.add(centre_change)
    db.session.commit()
    return "Information updated"

@app.route("/delete<int:id")
def delete(id):
    centre_change = climbing_centre.query.filter_by(id=id)
    db.session.delete(centre_change)
    return "Climber Centre Deleted"

