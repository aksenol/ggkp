from shared import db

vote = db.Table('vote',
	db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
	db.Column('comment_id', db.Integer, db.ForeignKey('comment.comment_id'),
	db.Column('time',db.DateTime),
	db.Column('is_upvote',db.Boolean))
)

