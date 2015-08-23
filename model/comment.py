from shared import db
from datetime import datetime

vote = db.Table('vote',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('comment_id', db.Integer, db.ForeignKey('comment.comment_id')),
    db.Column('time',db.DateTime),
    db.Column('is_upvote',db.Boolean)
)

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'))
    reply_to = db.Column(db.Integer, db.ForeignKey('comment.comment_id'))
    message = db.Column(db.String(5000))
    publish_date = db.Column(db.DateTime)

    votes = db.relationship('User', secondary=vote)
  
    def __init__(self, message, reply_to, user_id, post_id):
        self.message = message
        self.reply_to = reply_to
        self.user_id  = user_id
        self.post_id = post_id

    def __repr__(self):
        return '<Comment %r>' % self.comment_id

    def get_popular_comments(post_id): # -> comment[]
        pass

    def get_newest_comments(post_id): # -> comment[]
        pass

    def get_trending_comments(post_id): # -> comment[]
        pass

    def write_comment(post_id, text, reply_to=''): # -> comment_id
        pass

    def vote_comment(is_up, comment_id, user_id):
        pass
