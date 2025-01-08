from django.contrib.auth.views import LogoutView
from django.urls import include, path
from pacientes import admin
from pacientes import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # Asegúrate de que la app 'usuarios' está incluida correctamente
    path('pacientes/', include('pacientes.urls')),  # La app 'pacientes' también está incluida
    path('', include('usuarios.urls')),  # Si la página de inicio es del login
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('perfil/', include('perfiles.urls')),
    path('avatar/', include('avatar.urls')),
    path('mensajes/', include ('mensajes.urls')),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

