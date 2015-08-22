from shared import db
from vote import vote
class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))
    reply_to = db.Column(db.Integer, db.ForeignKey('comment.comment_id'))
   	message = db.Column(db.String(5000))
   	publish_date = db.Column(db.DateTime)

    votes = db.relationship('User', secondary=vote)
  

    def __init__(self):
    	pass

    def __repr__(self):
        return '<Comment %r>' % self.comment_id