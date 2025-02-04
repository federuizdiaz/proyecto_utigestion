from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Chat(models.Model):

    user_chat_1    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_user_1')
    user_chat_2    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_user_2')
    fecha_creacion = models.DateField(auto_now=False, auto_now_add=True)


class Mensaje(models.Model):

    chat       = models.ForeignKey(Chat, on_delete=models.CASCADE)
    de_user    = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contenido  = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField(auto_now_add=True, auto_now=False)
