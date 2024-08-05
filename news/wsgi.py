"""
WSGI config for news project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Loyihangiz yo'lini to'g'ri kiriting
path = '/home/DarkLight2008/sshsh'
if path not in sys.path:
    sys.path.append(path)

# Django sozlamalar modulin i o'rnatish
os.environ['DJANGO_SETTINGS_MODULE'] = 'news.settings'

# WSGI ilovasini olish
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
