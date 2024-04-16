import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret'
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/microblog'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  MAIL_SERVER = os.environ.get('MAIL_SERVER')
  MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
  MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  ADMINS = ['olayinkayakub@yahoo.com']
  POSTS_PER_PAGE = 3
  LANGUAGES = ['en', 'es']
