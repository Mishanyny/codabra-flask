from . import profile
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm, AddPost
from flask_login import current_user, login_user, logout_user
from .models import User, Posts


NAME = 'Misha'

@profile.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile.about'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user is None:
            flash('Invalid username')
            return redirect(url_for('profile.login'))
        login_user(user)
        return redirect(url_for('profile.main_page'))
    return render_template('login.html', form=form)


@profile.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.about'))


@profile.route('/')
def about():
    return render_template("about.html", name = NAME)


@profile.route('/main_page/<int:user_id>/')
@profile.route('/main_page/', defaults={'user_id': 0})
def main_page(user_id):
    if not user_id:
        if not current_user.is_authenticated:
            return redirect(url_for('profile.login'))
        return render_template("profile.html", user = current_user)
    else:
        user = User.objects(user_id = str(user_id)).first()
        if user is None:
            return render_template("about.html", name = NAME)
        else:
            return render_template("profile.html", user = user)


@profile.route('/message/',  methods=['GET', 'POST'])
def message():
    if not current_user.is_authenticated:
        return redirect(url_for('profile.login'))
    posts_list = []
    posts = Posts.objects[:20]
    for post in posts:
        sender = User.objects(user_id=post.user_id).first()

        posts_list.append({
            'user_name' : sender.username,
            'text' : post.text,
            'header' : post.header,
            'user_id' : sender.user_id
                        })
    form = AddPost()
    if form.validate_on_submit():
        post = Posts(
            user_id = current_user.user_id,
            text = form.posttext.data,
            header = form.posthead.data
                    )
        post.save()

    return render_template("message.html", posts=posts_list, form=form, check=current_user.is_authenticated)


@profile.route('/friends/')
def friends():
    if not current_user.is_authenticated:
        return redirect(url_for('profile.login'))
    return render_template("friends.html")


@profile.route('/settings/')
def settings():
    if not current_user.is_authenticated:
        return redirect(url_for('profile.login'))
    return render_template("settings.html")
    
