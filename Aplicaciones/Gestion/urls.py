from django.urls import path
from .import views

urlpatterns = [
    path('', views.inicio),

    # Rutas para EQUIPOS
    path('equipos/', views.listarEquipos),
    path('nuevoEquipo/', views.nuevoEquipo),
    path('guardarEquipo/', views.guardarEquipo),
    path('editarEquipo/<id>/', views.editarEquipo),
    path('eliminarEquipo/<id>/', views.eliminarEquipo),
    path('actualizarEquipo/', views.procesarEdicionEquipo),

    # Rutas para JUGADORES
    path('jugadores/', views.listarJugadores),
    path('nuevoJugador/', views.nuevoJugador),
    path('guardarJugador/', views.guardarJugador),
    path('editarJugador/<id>/', views.editarJugador),
    path('eliminarJugador/<id>/', views.eliminarJugador),
    path('actualizarJugador/', views.procesarEdicionJugador),
]

