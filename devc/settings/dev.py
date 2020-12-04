from ._base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = BASE_DIR / 'staticfiles'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
