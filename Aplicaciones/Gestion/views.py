from django.shortcuts import render, redirect
from .models import Equipo, Jugador 
from django.contrib import messages
# Create your views here.

#Mostrar la lista de equipos
def listarEquipos(request):
    equipos=Equipo.objects.all()
    return render (request, "equipos.html",{'equipos': equipos})

#Mostrar formulario de nuevos equipos 
def nuevoEquipo(request):
    return render(request, "nuevoEquipo.html")

# Guardar un nuevo equipo
def guardarEquipo(request):
    nombre = request.POST["nombre"]
    ciudad = request.POST["ciudad"]
    entrenador = request.POST["entrenador"]
    escudo_subido = request.FILES.get("escudo", None)

    nuevo_equipo = Equipo.objects.create(
        nombre=nombre,
        ciudad=ciudad,
        entrenador=entrenador,
        escudo=escudo_subido
    )
    messages.success(request, "Equipo guardado exitosamente")
    return redirect('/')

# Eliminar un equipo por su ID
def eliminarEquipo(request, id):
    equipo= Equipo.objects.get(id=id)
    
    # Eliminar el archivo de imagen del sistema si existe
    if equipo.escudo:
        equipo.escudo.delete()
    
    equipo.delete()
    messages.success(request, "Equipo eliminado exitosamente")
    return redirect('/')

 #Vista para la edición del equipo
def procesarEdicionEquipo(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    ciudad = request.POST["ciudad"]
    entrenador = request.POST["entrenador"]

    equipo = Equipo.objects.get(id=id)
    equipo.nombre = nombre
    equipo.ciudad = ciudad
    equipo.entrenador = entrenador

    if "escudo" in request.FILES:
        equipo.escudo = request.FILES["escudo"]

    equipo.save()
    messages.success(request, "Equipo actualizado exitosamente")
    return redirect('/')
    

    
