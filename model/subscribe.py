from shared import db

subscribe = db.Table('subscribe',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('group_id', db.Integer, db.ForeignKey('group.group_id'),
    db.Column('time',db.DateTime),
    db.Column('is_submitter',db.Boolean))
)

