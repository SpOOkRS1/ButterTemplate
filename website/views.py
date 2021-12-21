from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Project
from . import db
from flask_wtf.csrf import CSRFError
from .forms import ProjectForm, p_ProjectForm

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html")

# error handler 
@views.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


# Switch views
@views.route('/choice')
def switch1():
  return render_template('/switches/switch1.html')

# company switch
@views.route('/company_s')
def company_switch():
  project_type = None
  company_name= None
  company_email = None
  project_size = None
  form = ProjectForm()
  if form.validate_on_submit():
    project_type = form.project_type.data
    company_name = form.company_name.data
    company_email = form.company_email.data
  return render_template('/switches/companySwitch.html', project_type = project_type, company_name=company_name, company_email=company_email, project_size = project_size, form = form)

# personal switch
@views.route('/personal_s')
def personal_switch():
  project_type = None
  first_name= None
  email = None
  project_size = None
  form = p_ProjectForm()
  if form.validate_on_submit():
    project_type = form.project_type.data
    first_name = form.first_name.data
    email = form.email.data
  return render_template('/switches/personalSwitch.html', project_type = project_type, first_name=first_name, email=email, project_size = project_size, form = form)