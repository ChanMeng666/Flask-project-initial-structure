from eoms import app
from flask import render_template, redirect, request, flash, url_for
from eoms.form.example_form import RegistrationForm, LoginForm
from eoms.model import auth
from eoms.model.session_utils import allow_role

@app.route('/')
def home_t():
    return render_template('home_t.html')

@app.route('/register_t', methods=['GET', 'POST'])
def register_t():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        if auth.add_user(form.username.data, form.password.data):
            flash('Thanks for registering', 'success')
            return redirect(url_for('login_t'))
        else:
           flash('Regitration failed. Please try again.', 'danger') 
    return render_template('register_t.html', form=form)

@app.route('/login_t', methods=['GET', 'POST'])
def login_t():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        if auth.login_by_username(form.username.data, form.password.data):
            return redirect(url_for('profile_t'))
        else:
            error = "Invalid username or password. Please try again."
            return render_template("login_t.html", form=form, error=error)
    # If the request method is GET, display the login form
    else:
        return render_template("login_t.html", form=form)
    
@app.route('/profile_t')
def profile_t():
    allow_role(['customer'])
    return render_template("profile_t.html")
