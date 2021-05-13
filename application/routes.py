from flask import redirect, render_template, request, url_for
from application import app, db 
from application.models import ClimbingCentre
from application.forms import CentreForm

@app.route("/")
@app.route("/home")
def home():
    climbing_centres = ClimbingCentre.query.all()
    return render_template("index.html", centres=climbing_centres)

@app.route("/create", methods=["GET","POST"])
def create():
    form = CentreForm()
    if request.method == "POST":
        if form.validate_on_submit():
            centre = ClimbingCentre(centre_name=form.name.data, address=form.address.data)
            db.session.add(centre)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    form = CentreForm()
    if request.method == "POST":
        if form.validate_on_submit():
            centre = ClimbingCentre(centre_name=form.name.data, address=form.address.data)
            db.session.add(centre)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("update.html", form=form)
   

@app.route("/delete<int:id>", methods=["GET","DELETE","POST"])
def delete(id):
    centre_change = ClimbingCentre.query.filter_by(id=id)
    db.session.delete(centre_change)
    db.session.commit()
    return redirect(url_for("home"))


