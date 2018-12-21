import os

from decouple import config
from gwa_framework.redis import RedisServer
from gwa_framework.utils.encoders import UUIDEncoder

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = config('DEBUG', cast=bool)


GWA_ENVIRONMENT = config('GWA_ENVIRONMENT')
GWA_KEY = config('GWA_KEY')
GWA_CONSUMER_KEY = config('GWA_CONSUMER_KEY')


class GWAAppConfig:

    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = DatabaseConfig.get_uri()
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['RESTFUL_JSON'] = {'cls': UUIDEncoder}
        # app.config['ELASTIC_APM'] = {
        #     'SERVICE_NAME': ElasticApmConfig.SERVICE_NAME,
        #     'SECRET_TOKEN': ElasticApmConfig.SECRET_TOKEN,
        #     'SERVER_URL': ElasticApmConfig.SERVER_URL,
        #     'DEBUG': DEBUG,
        # }


# class ElasticApmConfig:
#     SERVICE_NAME = config('ELASTIC_APM_SERVICE_NAME')
#     SECRET_TOKEN = config('ELASTIC_APM_SECRET_TOKEN')
#     SERVER_URL = config('ELASTIC_APM_SERVER_URL')


class DatabaseConfig:
    DB_HOST = config('DB_HOST')
    DB_USER = config('DB_USER')
    DB_PASSWORD = config('DB_PASSWORD')
    DB_NAME = config('DB_NAME')

    @staticmethod
    def get_uri():
        return f"postgresql://{DatabaseConfig.DB_USER}:{DatabaseConfig.DB_PASSWORD}" \
               f"@{DatabaseConfig.DB_HOST}/{DatabaseConfig.DB_NAME}"


class LoggerSettings:
    LOGGER_NAME = f"gwa-{GWA_KEY}"
    LOGGER_APPLICATION = f"{GWA_KEY}"
    LOGGER_PRODUCT = f"gwa"
    LOGGER_OUTPUT_FORMAT = 'JSON'


class PubSubSettings:
    HOST = config('PUB_SUB_HOST')
    PORT = config('PUB_SUB_PORT')
    GROUP_ID = config('PUB_SUB_GROUP_ID')
    TOPICS = {
        'GOAL': f'{GWA_ENVIRONMENT}-{GWA_CONSUMER_KEY}-goals'
    }


class Cache(RedisServer):
    REDIS_HOST = config('CACHE_HOST')
    REDIS_PORT = config('CACHE_PORT')
