from django.urls import path
from .import views

urlpatterns = [
    # Rutas para Equipos
    path('equipos/', views.listarEquipos, name="listar_equipos"),
    path('equipos/nuevo/', views.nuevoEquipo, name="nuevo_equipo"),
    path('equipos/guardar/', views.guardarEquipo, name="guardar_equipo"),
    path('equipos/editar/<int:id>/', views.editarEquipo, name="editar_equipo"),
    path('equipos/actualizar/', views.procesarEdicionEquipo, name="actualizar_equipo"),
    path('equipos/eliminar/<int:id>/', views.eliminarEquipo, name="eliminar_equipo"),

    # Rutas para Jugadores
    path('jugadores/<int:id_equipo>/', views.listarJugadoresPorEquipo, name="listar_jugadores"),
    path('jugadores/nuevo/<int:id_equipo>/', views.nuevoJugador, name="nuevo_jugador"),
    path('jugadores/guardar/', views.guardarJugador, name="guardar_jugador"),
    path('jugadores/editar/<int:id>/', views.editarJugador, name="editar_jugador"),
    path('jugadores/actualizar/', views.procesarEdicionJugador, name="actualizar_jugador"),
    path('jugadores/eliminar/<int:id>/', views.eliminarJugador, name="eliminar_jugador"),

]

