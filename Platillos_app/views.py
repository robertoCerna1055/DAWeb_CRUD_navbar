from django.shortcuts import render,redirect
from .models import Platillo

# Create your views here.

def inicio_vistaPlatillos(request):
    losplatillos = Platillo.objects.all()

    return render(request,"gestionarPlatillo.html",{"misplatillos":losplatillos})



def registrarPlatillo(request):
    id_platillo = request.POST["txtidplatillo"]
    nombre_platillo = request.POST["txtdnombresplatillo"]
    descripcion = request.POST["txtdescripcion"]
    ingredientes = request.POST["txtingredientes"]
    precio = request.POST["txtprecio"]
    calorias = request.POST["txtcalorias"]
    tipo = request.POST["txttipo"]
    cantidad = request.POST["txtcantidad"]

    guardarplatillo = Platillo.objects.create(id_platillo=id_platillo, nombre_platillo=nombre_platillo, descripcion=descripcion,
                                        ingredientes=ingredientes, precio=precio, calorias=calorias, tipo=tipo, cantidad=cantidad)

    return redirect("platillos")

def seleccionarPlatillo(request, id_platillo):
    platillo = Platillo.objects.get(id_platillo = id_platillo)

    return render(request,"editarPlatillo.html",{"misplatillos":platillo})


def editarPlatillo(request):
    id_platillo = request.POST["txtidplatillo"]
    nombre_platillo = request.POST["txtnombresplatillo"]
    descripcion = request.POST["txtdescripcion"]
    ingredientes = request.POST["txtingredientes"]
    precio = request.POST["txtprecio"]
    calorias = request.POST["txtcalorias"]
    tipo = request.POST["txttipo"]
    cantidad = request.POST["txtcantidad"]

    platillo = Platillo.objects.get(id_platillo = id_platillo)
    platillo.nombre_platillo = nombre_platillo
    platillo.descripcion = descripcion
    platillo.ingredientes = ingredientes
    platillo.precio = precio
    platillo.calorias = calorias
    platillo.tipo = tipo
    platillo.cantidad = cantidad

    platillo.save()

    return redirect("platillos")


def borrarPlatillo(request, id_platillo):
    platillo = Platillo.objects.get(id_platillo = id_platillo)
    platillo.delete()

    return redirect("platillos")