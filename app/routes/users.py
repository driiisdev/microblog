from flask import render_template
from app import app
from app.models import User
from app.forms import EmptyForm
from flask_login import  login_required


@app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  posts = [
  {'author': user, 'body': 'Test post #1'},
  {'author': user, 'body': 'Test post #2'}
  ]
  form = EmptyForm()
  return render_template('user.html', user=user, posts=posts, form=form)
