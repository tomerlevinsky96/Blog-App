from flask import Blueprint, render_template, redirect, url_for, request, flash,make_response
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SignUpForm, LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form=LoginForm()
        email=form.email.data
        password=form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        form = SignUpForm()
        email=form.email.data
        firstName=form.FirstName.data
        lastName=form.LastName.data
        password=form.password.data
        BirthDate =form.Birthday.data

        email_exists = User.query.filter_by(email=email).first()
        if email_exists:
            flash('Email is already in use.', category='error')
        elif len(email) < 4:
            flash("Email is invalid.", category='error')
        else:
            new_user = User(email=email,FirstName=firstName,LastName=lastName,password=generate_password_hash(
                password, method='sha256'), BirthDay=BirthDate)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)

@auth.route("/about")
def about():
 return render_template("about.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))








