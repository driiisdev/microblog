from flask import flash, redirect, url_for
from app import app, db
from app.models import User
from app.forms import EmptyForm
from flask_login import current_user, login_required


@app.route('/follow/<username>', methods=['POST'])
@login_required
def follow(username):
  form = EmptyForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=username).first()
    if user is None:
      flash('User {} not found.'.format(username))
      return redirect(url_for('index'))
    if user == current_user:
      flash('You cannot follow yourself!')
      return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))
  else:
    return redirect(url_for('index'))
  
@app.route('/unfollow/<username>', methods=['POST'])
@login_required
def unfollow(username):
  form = EmptyForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=username).first()
    if user is None:
      flash('User {} not found.'.format(username))
      return redirect(url_for('index'))
    if user == current_user:
      flash('You cannot unfollow yourself!')
      return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))
  else:
    return redirect(url_for('index'))
