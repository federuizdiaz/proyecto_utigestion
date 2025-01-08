from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    ESPECIALIDADES = [
        ('Admision', 'Admision'),
        ('Clínica', 'Clínica'),
        ('Enfermería', 'Enfermería'),
        ('Pediatría', 'Pediatría'),
        ('Cardiología', 'Cardiología'),
        ('Traumatología', 'Traumatología'),
        ('Anestesiología', 'Anestesiología'),
        ('Terapia Intensiva', 'Terapia Intensiva'),
        ('Cirujia General', 'Cirugia General'),
        ('Imagenología', 'Imagenología'),
    ]
    especialidad = models.CharField(
        max_length=50,
        choices=ESPECIALIDADES,
        blank=True,
        null=True,
        verbose_name="Especialidad"
    )

    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")
    direccion = models.CharField(max_length=150, blank=True, null=True, verbose_name="Dirección")
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
    nombre = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nombre")  # Nuevo campo
    apellido = models.CharField(max_length=50, blank=True, null=True, verbose_name="Apellido")  # Nuevo campo
    nro_matricula_profesional = models.CharField(max_length=20, blank=True, null=True, verbose_name="Nro de Matrícula Profesional")  # Nuevo campo
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}" if self.nombre and self.apellido else self.username

