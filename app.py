from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from model.shared import db
from model.user import User
from model.group import Group
from model.post import Post
from model.comment import Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:43152957@localhost/ggkp"
db.init_app(app)

@app.route('/gitupdate')
def gitupdate():
	import subprocess
	cmd = ["git","pull"]
	p = subprocess.Popen(
			cmd, 
			stdout = subprocess.PIPE,
			stderr=subprocess.PIPE,
			stdin=subprocess.PIPE)
	out,err = p.communicate()
	return out

@app.route('/dbreset')
def dbreset():
	db.drop_all()
	db.create_all()
	return 'Database tables are reset'

db.init_app(app)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=4457,debug=True)

