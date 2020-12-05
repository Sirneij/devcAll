from ._base import *
from decouple import config
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# aws settings
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = None
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# s3 static settings
STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.us-east-2.amazonaws.com/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'devc.storage_backends.StaticStorage'
# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.us-east-2.amazonaws.com/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'devc.storage_backends.PublicMediaStorage'

# Heroku: Update database configuration from $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
