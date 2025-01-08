from django.urls import path
from mensajes.views import ver_chats, iniciar_chat, ver_chat


urlpatterns = [
    path('', ver_chats, name='ver_chats'),
    path('nuevo/', iniciar_chat, name='nuevo_chat'),
    path('chat/<int:id>/mensajes/', ver_chat, name='ver_chat'),
    ]