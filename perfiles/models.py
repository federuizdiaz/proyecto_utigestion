from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil',
        verbose_name='Usuario'
    )
    imagen = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Imagen de Perfil')
    link_web = models.URLField(blank=True, null=True, verbose_name='Enlace a una página web')
    email = models.EmailField(blank=True, null=True, verbose_name='Correo Electrónico')
    website = models.URLField(blank=True, null=True, verbose_name='Sitio Web')

    
    def __str__(self):
        return self.usuario.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crear_perfil_automatico(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)