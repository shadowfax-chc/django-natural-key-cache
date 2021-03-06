# vim: set et ts=4 sw=4 fileencoding=utf-8:
'''
Django settings for test project
'''
import os
import dj_config_url
from getenv import env

PROJ_ROOT = os.path.dirname(__file__)

SECRET_KEY = 'not_so_secret'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJ_ROOT, 'test.db'),
    },
}

INSTALLED_APPS = (
    'test_app',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

CACHE_URI = env('TEST_CACHE_URI', 'memcache://127.0.0.1:11211')
CUSTOM_CACHE_BACKEND = env('TEST_CACHE_BACKEND')

CACHES = {
    'default': dj_config_url.parse(CACHE_URI)
}
if CUSTOM_CACHE_BACKEND:
    CACHES['default']['BACKEND'] = CUSTOM_CACHE_BACKEND

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
        'simple': {
            'format': "%(levelname)s [%(name)s:%(lineno)s] %(message)s",
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
            'level': 'ERROR',
        },
        'factory': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'ERROR',
        },
        'natural_key_cache': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'ERROR',
        },
    },
}

MIDDLEWARE_CLASSES = ()
