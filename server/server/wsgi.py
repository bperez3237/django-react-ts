"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

# Get the root directory of your Django project
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the "server" directory to the Python path
APPS_DIR = os.path.join(ROOT_DIR, 'server')
sys.path.append(APPS_DIR)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()
