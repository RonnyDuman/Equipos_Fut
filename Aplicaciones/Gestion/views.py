from django.shortcuts import render, redirect
from .models import Equipo, Jugador 
from django.contrib import messages
# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')

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
    return redirect('/equipos/')

# Eliminar un equipo por su ID
def eliminarEquipo(request, id):
    equipo= Equipo.objects.get(id=id)
    
    # Eliminar el archivo de imagen del sistema si existe
    if equipo.escudo:
        equipo.escudo.delete()
    
    equipo.delete()
    messages.success(request, "Equipo eliminado exitosamente")
    return redirect('/equipos/')

# Mostrar el formulario para editar un equipo existente
def editarEquipo(request, id):
    equipo = Equipo.objects.get(id=id)
    return render(request, "editarEquipo.html", {'equipo': equipo})

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
    return redirect('/equipos/')


#Vista para Jugador


# Mostrar lista de jugadores por equipo
def listarJugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadores.html', {'jugadores': jugadores})
#Formulario para registrar nuevo jugador

def nuevoJugador(request):
    equipos = Equipo.objects.all()
    return render(request, 'nuevoJugador.html', {'equipos': equipos})
    
#Guardar nuevo jugador
def guardarJugador(request):
    equipo_id = request.POST.get("equipo_id")

    if not equipo_id:
        messages.error(request, "Debe seleccionar un equipo.")
        return redirect('/nuevoJugador/')  # Redirige al formulario

    nombre = request.POST.get("nombre")
    posicion = request.POST.get("posicion")
    numero_camiseta = request.POST.get("numero_camiseta")
    foto = request.FILES.get("foto")
    ficha_pdf = request.FILES.get("ficha_pdf")

    equipo = Equipo.objects.get(id=equipo_id)

    Jugador.objects.create(
        nombre=nombre,
        posicion=posicion,
        numero_camiseta=numero_camiseta,
        foto=foto,
        ficha_pdf=ficha_pdf,
        equipo=equipo
    )

    messages.success(request, "Jugador guardado exitosamente")
    return redirect(f'/jugadores/')




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
    return redirect(f'/jugadores/')


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
    return redirect(f'/jugadores/')

