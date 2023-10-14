import os 

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kopa_do_mundo.settings")

application = get_asgi_application()