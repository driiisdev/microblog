from flask import request, render_template, flash, redirect, url_for
from app import app, db
from app.forms import EditProfileForm
from flask_login import current_user, login_required

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
  form = EditProfileForm(current_user.username)
  if form.validate_on_submit():
    current_user.username = form.username.data
    current_user.about_me = form.about_me.data
    db.session.commit()
    flash('Your changes have been saved.')
    return redirect(url_for('edit_profile'))
  elif request.method == 'GET':
    form.username.data = current_user.username
    form.about_me.data = current_user.about_me
    
  return render_template('edit_profile.html', title='Edit Profile', form=form)
