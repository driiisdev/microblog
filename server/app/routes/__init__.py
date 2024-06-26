from flask import g
from flask_babel import get_locale
from app import app,db
from datetime import datetime
from flask_login import current_user

@app.before_request
def before_request():
  g.locale = str(get_locale())
  if current_user.is_authenticated:
    current_user.last_seen = datetime.utcnow()
    db.session.commit()
    
from app.routes.page import index
from app.routes.login import login
from app.routes.logout import logout
from app.routes.register import register
from app.routes.users import user
from app.routes.editProfile import edit_profile
from app.routes.followUnfollow import follow, unfollow
from app.routes.explore import explore
from app.routes.resetPasswordRequest import reset_password_request
