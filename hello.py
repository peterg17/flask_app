from flask import Flask, render_template
from flask import redirect


app = Flask(__name__)

#importing Flask-Script
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

#initializing the imported modules
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s</h1>' % user.name

@app.route('/user/magic')
def google():
	return redirect('http://www.google.com')


#nicer error handling
#REMEMBER TO ADD 404.html
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#REMEMBER TO ADD 500.html
@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500



if __name__ == '__main__':
	manager.run()




