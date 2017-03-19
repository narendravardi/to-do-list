# default config
import credentials


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = credentials.app_secret_key


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
