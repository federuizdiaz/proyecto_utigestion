from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagen', 'website', 'email']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

