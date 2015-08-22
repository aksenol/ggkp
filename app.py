from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://root:43152957@localhost/ggkp"
db = SQLAlchemy(app)

if __name__ == '__main__':
	app.run(host='127.0.0.1',port=4457,debug=True)

