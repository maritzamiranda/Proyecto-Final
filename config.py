class BaseConfig(object):
    # SQLALCHEMY_DATABASE_URI = "mysql://root:root@localhost:3306/compras_ventas"
    SQLALCHEMY_DATABASE_URI = "sqlite:///justin.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_POOL_SIZE = 20
    # SQLALCHEMY_POOL_TIMEOUT = 300
    SECRET_KEY = "horrible_secret_key"
    LOGIN_DISABLED = True