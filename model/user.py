from shared import db

subscribe = db.Table('subscribe',
	db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
	db.Column('group_id', db.Integer, db.ForeignKey('group.group_id'),
	db.Column('time',db.DateTime),
	db.Column('is_submitter',db.Boolean))
)

ban = db.Table('ban',
	db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
	db.Column('group_id', db.Integer, db.ForeignKey('group.group_id'),
	db.Column('banned_by', db.Integer, db.ForeignKey('user.user_id'),
	db.Column('time',db.DateTime),
	db.Column('is_shadow',db.Boolean))
)

class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	picture = db.Column(db.String(120))
	fb_token = db.Column(db.String(120))
	first_name = db.Column(db.String(80))
	last_name = db.Column(db.String(80))
	email = db.Column(db.String(80))
	age_range = db.Column(db.String(80))
	gender = db.Column(db.Integer)
	reg_date = db.Column(db.DateTime)
	
	posts = db.relationship('Post', backref = 'publisher', lazy = 'dynamic')
	groups = db.relationship('Group',
		secondary = subscribe, backref = db.backref('subscribers', lazy = 'dynamic'))
	banned_from = db.relationship('Group',
		secondary = ban, backref = db.backref('banned_users', lazy = 'dynamic'))
	admin_of = db.relationship('Group')

	def __init__(self):
		pass

	def __repr__(self):
		return '<User %r>' % self.user_id