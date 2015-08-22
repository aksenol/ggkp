from shared import db
class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
   	name = db.Column(db.String(120))
   	description = db.Column(db.String(120))
   	tag = db.Column(db.String(20))
	is_public = db.Column(db.Booelan)
	settings = db.Column(db.SmallInteger)
	creation_date = db.Column(db.DateTime)

	posts = db.relationship('Post', backref = 'group', lazy = 'dynamic')
	

    def __init__(self):
    	pass

    def __repr__(self):
        return '<Group %r>' % self.group_id