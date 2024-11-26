from django.shortcuts import render,redirect
from .models import Sucursal

# Create your views here.

def inicio_vistaSucursales(request):
    lassucursales = Sucursal.objects.all()

    return render(request,"gestionarSucursal.html",{"missucursales":lassucursales})



def registrarSucursal(request):
    id_sucursal = request.POST["txtidsucursal"]
    nombre_sucursal = request.POST["txtnombresucursal"]
    ubicacion = request.POST["txtubicacion"]
    horarios = request.POST["txthorarios"]
    celular = request.POST["txtcelular"]
    encargado = request.POST["txtencargado"]
    email = request.POST["txtemail"]

    guardarsucursal = Sucursal.objects.create(id_sucursal=id_sucursal, nombre_sucursal=nombre_sucursal, ubicacion=ubicacion,
                                              horarios=horarios, celular=celular, encargado=encargado, email=email)

    return redirect("sucursales")

def seleccionarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal = id_sucursal)

    return render(request,"editarSucursal.html",{"missucursales":sucursal})


def editarSucursal(request):
    id_sucursal = request.POST["txtidsucursal"]
    nombre_sucursal = request.POST["txtnombresucursal"]
    ubicacion = request.POST["txtubicacion"]
    horarios = request.POST["txthorarios"]
    celular = request.POST["txtcelular"]
    encargado = request.POST["txtencargado"]
    email = request.POST["txtemail"]

    sucursal = Sucursal.objects.get(id_sucursal = id_sucursal)
    sucursal.nombre_sucursal = nombre_sucursal
    sucursal.ubicacion = ubicacion
    sucursal.horarios = horarios
    sucursal.celular = celular
    sucursal.encargado = encargado
    sucursal.email = email

    sucursal.save()

    return redirect("sucursales")


def borrarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal = id_sucursal)
    sucursal.delete()

    return redirect("sucursales")