from django.shortcuts import render,redirect
from .models import Clientes

# Create your views here.

def inicio_vistaClientes(request):
    losclientes = Clientes.objects.all()

    return render(request,"gestionarClientes.html",{"misclientes":losclientes})



def registrarCliente(request):
    id_cliente = request.POST["txtidcliente"]
    nombre_cliente = request.POST["txtnombrecliente"]
    apellido_P = request.POST["txtapellidop"]
    apellido_M = request.POST["txtapellidom"]
    fecha_de_nacimiento = request.POST["txtfecha"]
    email = request.POST["txtemail"]
    celular = request.POST["txtcelular"]
    genero = request.POST["txtgenero"]

    guardarsucursal = Clientes.objects.create(id_cliente=id_cliente, nombre_cliente=nombre_cliente, apellido_P=apellido_P,
                                              apellido_M=apellido_M, fecha_de_nacimiento=fecha_de_nacimiento, email=email, celular=celular, genero=genero)

    return redirect("clientes")

def seleccionarCliente(request, id_cliente):
    clientes = Clientes.objects.get(id_cliente = id_cliente)

    return render(request,"editarClientes.html",{"misclientes":clientes})


def editarCliente(request):
    id_cliente = request.POST["txtidcliente"]
    nombre_cliente = request.POST["txtnombrecliente"]
    apellido_P = request.POST["txtapellidop"]
    apellido_M = request.POST["txtapellidom"]
    fecha_de_nacimiento = request.POST["txtfecha"]
    email = request.POST["txtemail"]
    celular = request.POST["txtcelular"]
    genero = request.POST["txtgenero"]

    trabajador = Clientes.objects.get(id_cliente = id_cliente)
    trabajador.nombre_cliente = nombre_cliente
    trabajador.apellido_P = apellido_P
    trabajador.apellido_M = apellido_M
    trabajador.email = email
    trabajador.fecha_de_nacimiento = fecha_de_nacimiento
    trabajador.celular = celular
    trabajador.genero = genero

    trabajador.save()

    return redirect("clientes")


def borrarCliente(request, id_cliente):
    clientes = Clientes.objects.get(id_cliente = id_cliente)
    clientes.delete()

    return redirect("clientes")