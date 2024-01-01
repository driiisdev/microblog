from app import app
from app.models import Post
from flask import request, render_template
from flask_login import login_required

@app.route('/explore')
@login_required
def explore():
  page = request.args.get('page', 1, type=int)
  posts = Post.query.order_by(Post.timestamp.desc()).paginate(
    page=page, per_page=app.config['POSTS_PER_PAGE'], error_out=False)
  return render_template('index.html', title='Explore', posts=posts)
