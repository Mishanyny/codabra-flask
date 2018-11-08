from .. import db
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Document):
    
    user_id = db.SequenceField()
    password_hash = db.StringField()
    full_name = db.StringField()
    username = db.StringField()
    city = db.StringField(default="")
    avatar_hash = db.StringField(default="")
    phone = db.StringField(default="")
    about_me = db.StringField(default="")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

    
