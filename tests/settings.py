# vim: set et ts=4 sw=4 fileencoding=utf-8:
import os
import sys

PROJ_ROOT = os.path.dirname(__file__)

SECRET_KEY = 'not_so_secret'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJ_ROOT, 'test.db'),
    },
}

INSTALLED_APPS = (
    'natural_key_cache',
    'tests',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '127.0.0.1:11211',
        ]
    },
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = False

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': ' [%(levelname)s] %(name)s: process_id="%(process)s";thread_id="%(thread)s": %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'factory': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'ERROR',
        },
        'natural_key_cache': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
    },
}

MIDDLEWARE_CLASSES = ()
