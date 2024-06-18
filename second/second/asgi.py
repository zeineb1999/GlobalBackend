

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')

application = get_asgi_application()

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from taches.urls import websocket_urlpatterns  # Importez les routes WebSocket de votre application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second.settings')

# Obtenez l'application ASGI de Django
django_asgi_application = get_asgi_application()

# Définissez le routeur des protocoles pour traiter les connexions HTTP et WebSocket
application = ProtocolTypeRouter({
    "http": django_asgi_application,  # Traitez les connexions HTTP avec l'application Django standard
    "websocket": AuthMiddlewareStack(
        URLRouter(
          websocket_urlpatterns  # Utilisez les routes WebSocket définies dans votre application
        )
    ),
})
 