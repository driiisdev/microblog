from app import app
from app.models import Post
from flask import request, render_template, url_for
from flask_login import login_required

@app.route('/explore')
@login_required
def explore():
  page = request.args.get('page', 1, type=int)
  posts = Post.query.order_by(Post.timestamp.desc()).paginate(
    page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
  next_url = url_for('explore', page=posts.next_num) \
    if posts.has_next else None
  prev_url = url_for('explore', page=posts.prev_num) \
    if posts.has_prev else None
  return render_template("index.html", title='Explore', 
    posts=posts.items, next_url=next_url, prev_url=prev_url)
