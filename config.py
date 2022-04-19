class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql://b03f89f8059b92:9f173f72@us-cdbr-east-05.cleardb.net/heroku_593e32d002747d8"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_POOL_TIMEOUT = 300
    SECRET_KEY = "horrible_secret_key"
    LOGIN_DISABLED = True