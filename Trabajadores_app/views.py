from django.shortcuts import render,redirect
from .models import Trabajadores

# Create your views here.

def inicio_vistaTrabajadores(request):
    lostrabajadores = Trabajadores.objects.all()

    return render(request,"gestionarTrabajador.html",{"mistrabajadores":lostrabajadores})



def registrarTrabajador(request):
    id_trabajador = request.POST["txtidtrabajador"]
    nombre_trabajador = request.POST["txtnombretrabajador"]
    apellido_P = request.POST["txtapellidop"]
    apellido_M = request.POST["txtapellidom"]
    email = request.POST["txtemail"]
    fecha_de_nacimiento = request.POST["txtfecha"]
    celular = request.POST["txtcelular"]
    genero = request.POST["txtgenero"]

    guardarsucursal = Trabajadores.objects.create(id_trabajador=id_trabajador, nombre_trabajador=nombre_trabajador, apellido_P=apellido_P,
                                              apellido_M=apellido_M, email=email, fecha_de_nacimiento=fecha_de_nacimiento, celular=celular, genero=genero)

    return redirect("trabajadores")

def seleccionarTrabajador(request, id_trabajador):
    trabajadores = Trabajadores.objects.get(id_trabajador = id_trabajador)

    return render(request,"editarTrabajador.html",{"mistrabajadores":trabajadores})


def editarTrabajador(request):
    id_trabajador = request.POST["txtidtrabajador"]
    nombre_trabajador = request.POST["txtnombretrabajador"]
    apellido_P = request.POST["txtapellidop"]
    apellido_M = request.POST["txtapellidom"]
    email = request.POST["txtemail"]
    fecha_de_nacimiento = request.POST["txtfecha"]
    celular = request.POST["txtcelular"]
    genero = request.POST["txtgenero"]

    trabajador = Trabajadores.objects.get(id_trabajador = id_trabajador)
    trabajador.nombre_trabajador = nombre_trabajador
    trabajador.apellido_P = apellido_P
    trabajador.apellido_M = apellido_M
    trabajador.email = email
    trabajador.fecha_de_nacimiento = fecha_de_nacimiento
    trabajador.celular = celular
    trabajador.genero = genero

    trabajador.save()

    return redirect("trabajadores")


def borrarTrabajador(request, id_trabajador):
    trabajador = Trabajadores.objects.get(id_trabajador = id_trabajador)
    trabajador.delete()

    return redirect("trabajadores")