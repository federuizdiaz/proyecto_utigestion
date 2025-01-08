from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class FormularioIniciarConversacion(forms.Form):

    user_chat_2 = forms.ModelChoiceField(
        queryset=User.objects.all(),  
        empty_label='',
        widget=forms.Select(attrs={ 'class' : 'form-control' }),
        label='Seleccionar Usuario',
        to_field_name='username'  
    )


class FormularioEnvioMensaje(forms.Form):

    contenido = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={ 'class' : 'form-control' }),
        label=''
    )
