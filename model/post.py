from shared import db
from datetime import datetime

seen = db.Table('seen',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.post_id')),
    db.Column('time',db.DateTime)
)

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    message = db.Column(db.String(5000))
    url = db.Column(db.String(120))
    settings = db.Column(db.SmallInteger)
    publish_date = db.Column(db.DateTime)
    publisher_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'))

    seen_by = db.relationship('User', secondary=seen)

    def __init__(self, message, url, settings, publisher_id, group_id):
        self.message = message
        self.url = url
        self.settings = settings
        self.publisher_id = publisher_id
        self.group_id = group_id
        self.publish_date = datetime.now()

    def __repr__(self):
        return '<Post %r>' % self.post_id