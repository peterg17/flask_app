from flask import Flask, render_template,session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'peter gregory'

#initializing the imported modules
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks like you have changed your name!')
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name=session.get('name'))



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




