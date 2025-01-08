from django.db import models
from django.conf import settings

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=8, unique=True)
    historia_clinica = models.TextField() 

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class EntradaEvolucion(models.Model):
    paciente = models.ForeignKey(Paciente, related_name='entradas_evolucion', on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='entradas_evolucion', on_delete=models.CASCADE)  
    asunto = models.CharField(max_length=255)
    texto_completo = models.TextField()
    imagen = models.ImageField(upload_to='entradas_evolucion/', null=True, blank=True) 
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.asunto
