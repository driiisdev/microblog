from flask import render_template, url_for, request
from app import app
from app.models import User, Post
from app.forms import EmptyForm
from flask_login import  login_required


@app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  page = request.args.get('page', 1, type=int)
  posts = user.posts.order_by(Post.timestamp.desc()).paginate(
    page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
  next_url = url_for('user', username=user.username, page=posts.next_num) \
    if posts.has_next else None
  prev_url = url_for('user', username=user.username, page=posts.prev_num) \
    if posts.has_prev else None
  form = EmptyForm()
  return render_template('user.html', user=user, posts=posts.items,
    next_url=next_url, prev_url=prev_url, form=form)
