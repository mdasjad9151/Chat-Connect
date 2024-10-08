"""
ASGI config for chatConnect project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# add
from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack

from chat.route import websocket_urlpatterns 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatConnect.settings')

application = get_asgi_application()

# add

application =  ProtocolTypeRouter({
    "http": application,
    "websocket": URLRouter(websocket_urlpatterns)
})
