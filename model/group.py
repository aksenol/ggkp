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

	def __init__(self, group):
		self.name = group.name
		self.description = group.description
		self.tag = group.tag
		self.is_public = group.is_public
		self.creator_id = group.creator_id
		self.settings = group.settings
		self.creation_date = datetime.now()

	def __repr__(self):
		return '<Group %r>' % self.group_id

	def get_hot_groups(self, page=0): # -> group_id []
		groups = Group.query.all()
		return [group.group_id for group in groups]

	def get_trending_groups(self, page=0): # -> group_id []
		groups = Group.query.all()
		return [group.group_id for group in groups]

	def	get_new_groups(self, page=0): # -> group_id []
		groups = Group.query.all()
		return [group.group_id for group in groups]

	def get_group(self, group_id): # -> group
		return Group.query.filter(Group.group_id == group_id).first()

	def create_group(self, group):
		temp = Group(group)
		db.session.add(temp)
		db.commit()
		return temp.group_id


