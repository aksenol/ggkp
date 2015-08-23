from shared import db
from datetime import datetime

subscribe = db.Table('subscribe',
	db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
	db.Column('group_id', db.Integer, db.ForeignKey('group.group_id')),
	db.Column('time',db.DateTime),
	db.Column('is_submitter',db.Boolean)
)

ban = db.Table('ban',
	db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
	db.Column('group_id', db.Integer, db.ForeignKey('group.group_id')),
	db.Column('banned_by', db.Integer, db.ForeignKey('user.user_id')),
	db.Column('time',db.DateTime),
	db.Column('is_shadow',db.Boolean)
)

class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	first_name = db.Column(db.String(80))
	last_name = db.Column(db.String(80))
	email = db.Column(db.String(80))
	picture = db.Column(db.String(120))
	age_range = db.Column(db.String(80))
	fb_token = db.Column(db.String(120))
	gender = db.Column(db.Integer)
	reg_date = db.Column(db.DateTime)
	
	posts = db.relationship('Post', backref = 'publisher', lazy = 'dynamic')
	subscribed_groups = db.relationship('Group',
		secondary = subscribe, backref = db.backref('subscribers', lazy = 'dynamic'))
	banned_from = db.relationship('Group',
		secondary = ban, backref = db.backref('banned_users', lazy = 'dynamic'))
	admin_of = db.relationship('Group')

	def __init__(self, first_name, last_name, email, picture, age_range, fb_token, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.picture = picture
		self.age_range = age_range 
		self.fb_token = fb_token
		self.gender = gender
		self.reg_date = datetime.now()

	def __repr__(self):
		return '<User %r>' % self.user_id

	def get_subscribed_groups(self, user_id, page=0): # -> group_id []
		user = User.query.filter(User.user_id == user_id).first()
        return [group.group_id for group in user.subscribed_groups]

	def subscribe_to(self, group_id, user_id, is_submitter): # -> bool	
		subscribe.insert().values(group_id=group_id, user_id=user_id, is_submitter=is_submitter,time=datetime.now())
		db.session.commit()
		return True

	def ban_user(self, group_id, admin_id, banned_by, is_shadow): # -> bool
		ban.insert().values(group_id=group_id, admin_id=admin_id, banned_by=banned_by, is_shadow=is_shadow,time=datetime.now())
		db.session.commit()
		return True


