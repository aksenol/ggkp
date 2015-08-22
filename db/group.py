from shared import db
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = usernamae
        self.email = email

    def __repr__(self):
        return '<Group %r>' % self.username