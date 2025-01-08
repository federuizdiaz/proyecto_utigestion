from django.urls import path
from .views import about, eliminar_entrada, ver_entrada_evolucion, inicio_pacientes, lista_pacientes, registrar_paciente, detalles_paciente, editar_entrada_evolucion

urlpatterns = [
    path('inicio_pacientes/', inicio_pacientes, name='inicio_pacientes'),
    path('lista_pacientes/', lista_pacientes, name='lista_pacientes'),
    path('registrar_paciente/', registrar_paciente, name='registrar_paciente'),
    path('paciente/<int:paciente_id>/', detalles_paciente, name='detalles_paciente'),
    path('entrada_evolucion/eliminar/<int:entrada_id>/', eliminar_entrada, name='eliminar_entrada'),
    path('entrada_evolucion/ver/<int:entrada_id>/', ver_entrada_evolucion, name='ver_entrada_evolucion'),
    path('entrada_evolucion/editar/<int:entrada_id>/', editar_entrada_evolucion, name='editar_entrada_evolucion'),
    path('about/', about, name='about'),
]
