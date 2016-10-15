import os
from mongoengine import connect


SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
]

DATABASES = {
    'default':
         {'ENGINE': 'django.db.backends.sqlite3',
          # 'NAME': 'test.db',
          'TEST_NAME': 'test.db',
          'USER': '',
          'PASSWORD': '',
          'HOST': '',
          'PORT': '',
          }
}

# MONGO
MONGO_DB_NAME = 'mongo_test'
MONGO_HOST = os.environ.get('MONGO_HOST', '')
db = connect(
	MONGO_DB_NAME,
    host=MONGO_HOST,
	port=27017,
    tz_aware=True)
db.drop_database(MONGO_DB_NAME)
