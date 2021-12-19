from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email
# Flask WTF form fields:
  # BooleanField
  # DateField - Date field just has date
  # DateTimeField - Date time has TIME 
  # DecimalField
  # FileField
  # HiddenField
  # MultipleField
  # FieldList
  # FloatField
  # FormField
  # IntegerField - Whole number
  # PasswordField
  # RadioField - radio button
  # SelectField - dropdown select 
  # SelectMultipleField
  # SubmitField
  # StringField
  # TextAreaField - "box" field

# Flask WTF Validators:
  # DataRequired
  # Email
  # EqualTo
  # InputRequired
  # IPAddress
  # Length
  # MacAddress
  # NumberRange
  # Optional
  # Regexp
  # URL
  # UUID - unique user identifier number
  # AnyOf
  # NoneOf


# create a form class
class ProjectForm(FlaskForm):
  project_type = SelectField(u'Project type: ', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
  company_name = StringField("Company name: ", validators=[DataRequired()])
  company_email = StringField("Company email: ", validataors=[Email])
  submit = SubmitField("Submit")
