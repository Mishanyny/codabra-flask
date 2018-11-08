from . import profile
from flask import render_template, flash, redirect
from .models import User


NAME = 'Misha'

@profile.route('/')
def about():
    return render_template("about.html", name = NAME)


@profile.route('/main_page/<int:user_id>/')
def main_page(user_id):
    user = User.objects(user_id = user_id).first()
    return render_template("profile.html", user = user)

@profile.route('/message/')
def message():
    return render_template("message.html")

@profile.route('/friends/')
def friends():
    return render_template("friends.html")

@profile.route('/settings/')
def settings():
    return render_template("settings.html")
    
