from shared import db

seen = db.Table('seen',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.post_id'),
    db.Column('time',db.DateTime))
)

