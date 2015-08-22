from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/gitupdate')
def gitupdate():
	import subprocess
	cmd = ["git","pull"]
	p = subprocess.Popen(cmd, stdout = subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
	out,err = p.communicate()
	return out

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://root:43152957@localhost/ggkp"
db = SQLAlchemy(app)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=4457,debug=True)

