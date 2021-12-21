from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired
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
  # project type
  project_type = SelectField(u'Project type: ', choices=[('ws', 'Website'), ('wa', 'Web App')])
  #project size
  project_size = SelectField(u'Project sized: ', choices=[('sm', 'Small'), ('med', 'Medium'), ('lg', 'Large')])
  # company name
  company_name = StringField("Company name: ", validators=[DataRequired()])
  # company email
  company_email = StringField("Company email: ", validators=[Email()])

  submit = SubmitField("Submit")


class p_ProjectForm(FlaskForm):
  # project type
  project_type = SelectField(u'Project type: ', choices=[('ws', 'Website'), ('wa', 'Web App')])
  #project size
  project_size = SelectField(u'Project sized: ', choices=[('sm', 'Small'), ('med', 'Medium'), ('lg', 'Large')])
  # company name
  first_name = StringField("First name: ", validators=[DataRequired()])
  # company email
  email = StringField("Email: ", validators=[Email()])

  submit = SubmitField("Submit")
