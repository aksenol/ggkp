from shared import db

ban = db.Table('ban',
	db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
	db.Column('group_id', db.Integer, db.ForeignKey('group.group_id'),
	db.Column('banned_by', db.Integer, db.ForeignKey('user.user_id'),
	db.Column('time',db.DateTime),
	db.Column('is_shadow',db.Boolean))
)

