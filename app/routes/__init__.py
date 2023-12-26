from app import app,db
from datetime import datetime
from flask_login import current_user

@app.before_request
def before_request():
  if current_user.is_authenticated:
    current_user.last_seen = datetime.utcnow()
    db.session.commit()
    
from app.routes.page import index
from app.routes.login import login
from app.routes.logout import logout
from app.routes.register import register
from app.routes.users import user
from app.routes.editProfile import edit_profile
