from django.shortcuts import render,redirect
from .models import Ventas

# Create your views here.

def inicio_vistaVentas(request):
    lasventas = Ventas.objects.all()

    return render(request,"gestionarVentas.html",{"misventas":lasventas})



def registrarVentas(request):
    id_venta = request.POST["txtidventa"]
    nombre_venta = request.POST["txtnombreventa"]
    fecha = request.POST["txtfecha"]
    hora = request.POST["txthora"]
    id_producto = request.POST["txtidproducto"]
    id_cliente = request.POST["txtidcliente"]
    id_trabajador = request.POST["txtidtrabajador"]
    cantidad = request.POST["txtcantidad"]
    registro = request.POST["txtregistro"]
    lugar = request.POST["txtlugar"]

    guardarventa = Ventas.objects.create(id_venta=id_venta, nombre_venta=nombre_venta, fecha=fecha,
                                              hora=hora, id_producto=id_producto, id_cliente=id_cliente, id_trabajador=id_trabajador, 
                                              cantidad=cantidad, registro=registro, lugar=lugar)

    return redirect("ventas")

def seleccionarVenta(request, id_venta):
    ventas = Ventas.objects.get(id_venta = id_venta)

    return render(request,"editarVentas.html",{"misventas":ventas})


def editarVentas(request):
    id_venta = request.POST["txtidventa"]
    nombre_venta = request.POST["txtnombreventa"]
    fecha = request.POST["txtfecha"]
    hora = request.POST["txthora"]
    id_producto = request.POST["txtidproducto"]
    id_cliente = request.POST["txtidcliente"]
    id_trabajador = request.POST["txtidtrabajador"]
    cantidad = request.POST["txtcantidad"]
    registro = request.POST["txtregistro"]
    lugar = request.POST["txtlugar"]

    venta = Ventas.objects.get(id_venta = id_venta)
    venta.nombre_venta = nombre_venta
    venta.fecha = fecha
    venta.hora = hora
    venta.id_producto = id_producto
    venta.id_cliente = id_cliente
    venta.id_trabajador = id_trabajador
    venta.cantidad = cantidad
    venta.registro = registro
    venta.lugar = lugar

    venta.save()

    return redirect("ventas")


def borrarVenta(request, id_venta):
    venta = Ventas.objects.get(id_venta = id_venta)
    venta.delete()

    return redirect("ventas")