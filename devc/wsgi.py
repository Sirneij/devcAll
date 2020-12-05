"""
WSGI config for devc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
# from django.conf import settings

from django.core.wsgi import get_wsgi_application
# if settings.DEBUG:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devc.settings.dev')
# else:
# os.environ.setdefault('DJANGO_SETTINGS_MODULE',
#                           'devc.settings.production')

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devc.settings')

application = get_wsgi_application()
