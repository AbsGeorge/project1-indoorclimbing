from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import Length



class CentreForm(FlaskForm):
    name = StringField("Name of Centre you visisted ", validators=[
        Length(min=1, max=50)
    ])

    address = StringField("What is the address of the centre you visited? ", validators=[
        Length(min=1, max=100)
    ])

    submit = SubmitField('Submit')

class ClimberForm(FlaskForm):
    climber_first_name = StringField("First name ", validators=[ 
        Length(min=1, max=50)])

    climber_last_name = StringField("Last name ", validators=[ 
        Length(min=1, max=50)])

    climber_email = StringField("Email address ", validators=[ 
        Length(min=1, max=100)])

    submit = SubmitField('Submit')

  