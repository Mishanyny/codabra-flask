from .. import db

class User(db.Document):

    user_id = db.SequenceField()
    full_name = db.StringField()
    nick_name = db.StringField()
    city = db.StringField(default="")
    avatar_hash = db.StringField(default="")
    phone = db.StringField(default="")
    about_me = db.StringField(default="")
    
