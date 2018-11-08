from . import profile
from flask import render_template, flash, redirect


NAME = 'Misha'

@profile.route('/')
def about():
    return render_template("about.html", name = NAME)


@profile.route('/main_page/')
def main_page():
    return render_template("profile.html", nickname = NAME, about_me = 'my name is misha')

@profile.route('/message/')
def message():
    return render_template("message.html")

@profile.route('/friends/')
def friends():
    return render_template("friends.html")

@profile.route('/settings/')
def settings():
    return render_template("settings.html")
    
