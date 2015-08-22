from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from db.shared import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://root:43152957@localhost/ggkp"


@app.route('/gitupdate')
def gitupdate():
	import subprocess
	cmd = ["git","pull"]
	p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
	out,err = p.communicate()
	return out

@app.route('/dbreset')
def dbreset():
	db.init_app(app)
	from db.user import User
	from db.user import Group
	db.drop_all()
	db.create_all()
	admin = User('admin', 'admin@example.com')
	guest = Group('guest', 'guest@example.com')
	db.session.add(admin)
	db.session.add(guest)
	db.session.commit()
	return User.query.all()


db.init_app(app)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=4457,debug=True)

