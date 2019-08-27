# /src/config.py

import os

class Development(object):
    DEBUG = True
    TESTING = False

class Production(object):
    DEBUG = False
    TESTING = False

app_config = {
    'development': Development,
    'production': Production,
}