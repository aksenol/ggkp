from shared import db
from datetime import datetime
from group import Group
from user import User

seen = db.Table('seen',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.post_id')),
    db.Column('time',db.DateTime)
)

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    message = db.Column(db.String(5000))
    url = db.Column(db.String(120))
    settings = db.Column(db.SmallInteger)
    publish_date = db.Column(db.DateTime)
    publisher_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'))

    seen_by = db.relationship('User', secondary=seen)
    comments = db.relationship('Comment', backref = 'post', lazy = 'dynamic')

    #backrefs
    #publisher -> submitted by
    #group -> submitted in 


    def __init__(self, post):
        self.message = post.message
        self.url = post.url
        self.settings = post.settings
        self.publisher_id = post.publisher_id
        self.group_id = post.group_id
        self.publish_date = datetime.now()

    def __repr__(self):
        return '<Post %r>' % self.post_id

    def get_hot_feed(self, group_id, page=0): # -> post_id[]
        group = Group.query.filter(Group.group_id == group_id).first()
        return [post.post_id for post in group.posts]

    def get_trending_feed(self, group_id, page=0): # -> post_id[]
        group = Group.query.filter(Group.group_id == group_id).first()
        return [post.post_id for post in group.posts]

    def get_new_feed(self, group_id, page=0): # -> post_id[]
        group = Group.query.filter(Group.group_id == group_id).first()
        return [post.post_id for post in group.posts]

    def get_post(self, post_id): # -> post
        return Post.query.filter(Post.post_id == post_id).first()

    def create_post(self, post): # -> post_id
        temp = Post(post)
        db.session.add(temp)
        db.commit()
        return temp.post_id

    def get_front_page(self, user_id): # -> post_id []
        user = User.query.filter(User.user_id == user_id).first()
        result = []
        for group in user.subscribed_groups:
            result.append([post.post_id for post in group.posts])
        return result