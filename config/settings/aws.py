from .base import *


STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

ALLOWED_HOSTS = ['*']

CHANNEL_LAYERS = {
     "default": {
         "BACKEND": "channels_redis.core.RedisChannelLayer",
         "CONFIG": {
            "hosts": [("redis", 6379)],
         },
     },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379?db=0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "COMPRESSOR": "django_redis.compressors.lz4.Lz4Compressor",
            "IGNORE_EXCEPTIONS": True,
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        },
        'TIMEOUT': MAX_CACHE_TIME,
        "KEY_PREFIX": '',
    }
}

CACHEOPS_REDIS = {
    'host': 'redis',
    'port': 6379,
    'db': 1,
}

CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'

DATABASES = {
    'default': {
        'ENGINE': 'postgres',
        'NAME': 'elogs',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'asu',
        'PASSWORD': '374tuamcPkf',
    },
}

DEBUG = False

#MIDDLEWARE.insert(1, 'django.middleware.gzip.GZipMiddleware')

#MIDDLEWARE = [] + MIDDLEWARE + \
#             [
#                 'htmlmin.middleware.HtmlMinifyMiddleware',
#                 'htmlmin.middleware.MarkRequestMiddleware',
#             ]
#HTML_MINIFY = True
