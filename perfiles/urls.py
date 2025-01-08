from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/borrar/', views.borrar_perfil, name='borrar_perfil'),
]
