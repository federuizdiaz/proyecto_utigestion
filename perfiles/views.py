from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import PerfilForm
from .models import Perfil
from django.http import Http404

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Perfil

@login_required
def ver_perfil(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    return render(request, 'perfiles/ver_perfil.html', {'perfil': perfil})


@login_required
def editar_perfil(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        
        password_form = None
        if 'password1' in request.POST and request.POST['password1']:
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
        
        if form.is_valid():
            form.save()
            
            if password_form and password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)
            
            return redirect('ver_perfil') 

    else:
        form = PerfilForm(instance=perfil)
        password_form = PasswordChangeForm(user=request.user)
    
    return render(request, 'perfiles/editar_perfil.html', {'form': form, 'password_form': password_form})

@login_required
def borrar_perfil(request):
    user = request.user
    user.delete()
    return redirect('home') 
