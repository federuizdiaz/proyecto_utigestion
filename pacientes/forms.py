from django import forms
from django.contrib.auth.forms import UserCreationForm
from pacientes.models import Paciente
from django import forms
from django import forms
from .models import EntradaEvolucion


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["nombre", "apellido", "fecha_nacimiento", "dni", "historia_clinica"]
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={"type": "date"}),
        }



class EntradaEvolucionForm(forms.ModelForm):
    class Meta:
        model = EntradaEvolucion
        fields = ['asunto', 'texto_completo', 'imagen']  # Añadimos 'imagen' al formulario
        widgets = {
            'texto_completo': forms.Textarea(attrs={'rows': 5, 'class': 'ckeditor'}),
        }
