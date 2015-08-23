from shared import db
from datetime import datetime
from post import Post

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

    #backrefs
    #post

    def __init__(self, comment):
        self.message = comment.message
        self.reply_to = comment.reply_to
        self.user_id  = comment.user_id
        self.post_id = comment.post_id
        self.publish_date = datetime.now()

    def __repr__(self):
        return '<Comment %r>' % self.comment_id

    def get_popular_comments(self, post_id): # -> comment[]
        post = Post.query.filter(Post.post_id == post_id).first()
        return [comment.comment_id for comment in post.comments]

    def get_newest_comments(self, post_id): # -> comment[]
        post = Post.query.filter(Post.post_id == post_id).first()
        return [comment.comment_id for comment in post.comments]

    def get_trending_comments(self, post_id): # -> comment[]
        post = Post.query.filter(Post.post_id == post_id).first()
        return [comment.comment_id for comment in post.comments]

    def write_comment(self, comment): # -> comment_id
        temp = Comment(comment)
        db.session.add(temp)
        db.session.commit()
        return temp.comment_id

    def vote_comment(self, is_upvote, comment_id, user_id):
        vote.insert().values(is_upvote=is_upvote,comment_id=comment_id,user_id = user_id, time=datetime.now())
        db.session.commit()
        return True
