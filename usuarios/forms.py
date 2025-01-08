from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "nombre", 
            "apellido", 
            "nro_matricula_profesional",
            "especialidad",   
            "email", 
            "telefono", 
            "direccion", 
            "fecha_nacimiento", 
            "password1", 
            "password2",
        )
        labels = {
            "username": "Nombre de usuario",
            "nombre": "Nombre",
            "apellido": "Apellido",
            "nro_matricula_profesional": "Número de Matrícula Profesional",
            "especialidad": "Especialidad",
            "email": "Correo electrónico",
            "telefono": "Teléfono",
            "direccion": "Dirección",
            "fecha_nacimiento": "Fecha de nacimiento",
                        
        }
