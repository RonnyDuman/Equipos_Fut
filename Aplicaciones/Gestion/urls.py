from django.urls import path
from .import views

urlpatterns = [
    # Rutas para EQUIPOS
    path('equipos/', views.listarEquipos, name="listar_equipos"),
    path('equipos/nuevo/', views.nuevoEquipo, name="nuevo_equipo"),
    path('equipos/guardar/', views.guardarEquipo, name="guardar_equipo"),
    path('equipos/editar/<int:id>/', views.editarEquipo, name="editar_equipo"),
    path('equipos/actualizar/', views.procesarEdicionEquipo, name="actualizar_equipo"),
    path('equipos/eliminar/<int:id>/', views.eliminarEquipo, name="eliminar_equipo"),


]

