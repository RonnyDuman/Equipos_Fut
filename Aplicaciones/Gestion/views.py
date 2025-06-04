from django.shortcuts import render, redirect
from .models import Equipo, Jugador 
from django.contrib import messages
# Create your views here.

#Vistas para Equipo

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


#Vista para Jugador


# Mostrar lista de jugadores por equipo
def listarJugadoresPorEquipo(request, id_equipo):
    equipo = Equipo.objects.get(id=id_equipo)
    jugadores = Jugador.objects.filter(equipo=equipo)
    return render(request, "jugadores.html", {
        'jugadores': jugadores,
        'equipo': equipo
    })

#Formulario para registrar nuevo jugador

def nuevoJugador(request, id_equipo):
    equipo=Equipo.objects.get(id=id_equipo)
    return render (request, "nuevoJugador.html", {'equipo':equipo})
    
#Guardar nuevo jugador
def guardarJugador(request):
    nombre = request.POST["nombre"]
    posicion = request.POST["posicion"]
    numero_camiseta = request.POST["numero_camiseta"]
    equipo_id = request.POST["equipo_id"]
    
    foto_subida = request.FILES.get("foto", None)
    ficha_pdf_subida = request.FILES.get("ficha_pdf", None)
    
    equipo = Equipo.objects.get(id=equipo_id)
    
    Jugador.objects.create(
        nombre=nombre,
        posicion=posicion,
        numero_camiseta=numero_camiseta,
        foto=foto_subida,
        ficha_pdf=ficha_pdf_subida,
        equipo=equipo
    )
    
    messages.success(request, "Jugador guardado exitosamente")
    return redirect(f'/jugadores/{equipo_id}/')

# Eliminar jugador
def eliminarJugador(request, id):
    jugador = Jugador.objects.get(id=id)
    id_equipo = jugador.equipo.id
    
    # Eliminar archivos si existen
    if jugador.foto:
        jugador.foto.delete()
    if jugador.ficha_pdf:
        jugador.ficha_pdf.delete()

    jugador.delete()
    messages.success(request, "Jugador eliminado exitosamente")
    return redirect(f'/jugadores/{id_equipo}/')


# Formulario de edición de jugador
def editarJugador(request, id):
    jugador = Jugador.objects.get(id=id)
    return render(request, "editarJugador.html", {'jugador': jugador})


# Procesar edición de jugador
def procesarEdicionJugador(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    posicion = request.POST["posicion"]
    numero_camiseta = request.POST["numero_camiseta"]

    jugador = Jugador.objects.get(id=id)
    jugador.nombre = nombre
    jugador.posicion = posicion
    jugador.numero_camiseta = numero_camiseta

    if "foto" in request.FILES:
        jugador.foto = request.FILES["foto"]

    if "ficha_pdf" in request.FILES:
        jugador.ficha_pdf = request.FILES["ficha_pdf"]

    jugador.save()
    messages.success(request, "Jugador actualizado exitosamente")
    return redirect(f'/jugadores/{jugador.equipo.id}/')