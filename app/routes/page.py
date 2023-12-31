from app import app, db
from flask import request, flash, redirect,render_template, url_for
from flask_login import current_user, login_required
from app.forms import PostForm
from app.models import Post

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
  form = PostForm()
  if form.validate_on_submit():
    post = Post(body=form.post.data, author=current_user)
    db.session.add(post)
    db.session.commit()
    flash('Your post is now live!')
    return redirect(url_for('index'))
  page = request.args.get('page', 1, type=int)
  posts = current_user.followed_posts().paginate(
    page, app.config['POSTS_PER_PAGE'], False)
  return render_template('index.html', title='Home', form=form,
    posts=posts.items)
