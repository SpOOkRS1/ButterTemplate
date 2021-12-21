from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .forms import ProjectForm
from flask_wtf.csrf import CSRFError

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Inncorrect password', category = 'error')
        else:
            flash('Email does not exist', category='error')
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Sign-up view
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  project_type = None
  company_name= None
  company_email = None
  project_size = None
  form = ProjectForm()
  if form.validate_on_submit():
    project_type = form.project_type.data
    company_name = form.company_name.data
    company_email = form.company_email.data
    
  return render_template('sign_up.html', project_type = project_type, company_name=company_name, company_email=company_email, project_size = project_size, form = form)

# CSRF Handler
@auth.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400