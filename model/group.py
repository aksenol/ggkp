from shared import db
from datetime import datetime

class Group(db.Model):
	group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(120))
	description = db.Column(db.String(120))
	tag = db.Column(db.String(20))
	is_public = db.Column(db.Boolean)
	creator_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
	settings = db.Column(db.SmallInteger)
	creation_date = db.Column(db.DateTime)

	posts = db.relationship('Post', backref = 'group', lazy = 'dynamic')

	#backrefs
	#subscribers -> list
	#banned_users -> list

	def __init__(self, name, description, tag, is_public, creator_id, settings):
		self.name = name
		self.description = description
		self.tag = tag
		self.is_public = is_public
		self.creator_id = creator_id
		self.settings = settings
		self.creation_date = datetime.now()

	def __repr__(self):
		return '<Group %r>' % self.group_id

	def get_hot_groups(page=0): # -> group_id []
		pass

	def get_trending_groups(page=0): # -> group_id []
		pass

	def	get_new_groups(page=0): # -> group_id []
		pass

	def get_group(group_id): # -> group
		pass

	def create_group(
			name, desc, is_public, creator_id, 
			tag='',picture='', settings=''): # -> group_id
		pass


