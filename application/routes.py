from flask import redirect, render_template, request, url_for
from application import app, db 
from application.models import ClimberInformation, ClimbingCentre
from application.forms import CentreForm, ClimberForm

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

@app.route("/signup/<int:id>", methods=["GET","POST"])
def signup(id):
    form = ClimberForm()
    if request.method == "POST":
        if form.validate_on_submit():
            climber = ClimberInformation(first_name=form.climber_first_name.data, last_name=form.climber_last_name.data, email=form.climber_email.data, centre_id=id)
            db.session.add(climber)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("signup.html", form=form)


@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    form = CentreForm()
    centre_update = ClimbingCentre.query.get(id)
    if request.method == "POST":
        if form.validate_on_submit():
            centre_update.centre_name = form.name.data
            centre_update.address = form.address.data
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("update.html", form=form, title="  - Update Centre Information", centre_update=centre_update)
   

@app.route("/delete/<int:id>", methods=["GET","DELETE"])
def delete(id):
    centre_delete = ClimbingCentre.query.get(id)
    db.session.delete(centre_delete)
    db.session.commit()
    return redirect(url_for("home"))


