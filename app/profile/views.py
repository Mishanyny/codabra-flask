from . import profile
from flask import render_template, redirect, session, url_for, g, flash
from .models import User
from .forms import LoginForm
from flask_login import current_user, login_user, logout_user
from .models import User
from .forms import RegistrationForm

NAME = 'Misha'


@profile.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile.about'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('profile.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('profile.main_page'))
    return render_template('login.html', form=form)


@profile.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile.about'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        user.save()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('profile.login'))
    return render_template('register.html', form=form)


@profile.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.about'))


@profile.route('/about/')
@profile.route('/')
def about():
    if not current_user.is_authenticated:
        return redirect(url_for('profile.login'))
    return render_template("about.html", name = NAME)


@profile.route('/main_page/')
def main_page():
    if not current_user.is_authenticated:
        return redirect(url_for('profile.login'))
    return render_template("profile.html", user = current_user)

@profile.route('/message/')
def message():
    return render_template("message.html")

@profile.route('/friends/')
def friends():
    return render_template("friends.html")

@profile.route('/settings/')
def settings():
    return render_template("settings.html")
    
