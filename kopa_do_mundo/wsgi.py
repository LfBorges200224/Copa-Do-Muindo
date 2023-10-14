import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kopa_do_mundo.settings')

application = get_wsgi_application()