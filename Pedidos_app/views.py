from django.shortcuts import render,redirect
from .models import Pedidos

# Create your views here.

def inicio_vistaPedidos(request):
    lospedidos = Pedidos.objects.all()

    return render(request,"gestionarPedidos.html",{"mispedidos":lospedidos})



def registrarPedidos(request):
    id_pedido = request.POST["txtidpedido"]
    nombre_pedido = request.POST["txtnombrepedido"]
    fecha = request.POST["txtfecha"]
    hora = request.POST["txthora"]
    id_producto = request.POST["txtidproducto"]
    id_cliente = request.POST["txtidcliente"]
    id_trabajador = request.POST["txtidtrabajador"]
    cantidad = request.POST["txtcantidad"]
    registro = request.POST["txtregistro"]

    guardarventa = Pedidos.objects.create(id_pedido=id_pedido, nombre_pedido=nombre_pedido, fecha=fecha,
                                              hora=hora, id_producto=id_producto, id_cliente=id_cliente, id_trabajador=id_trabajador, 
                                              cantidad=cantidad, registro=registro)

    return redirect("pedidos")

def seleccionarPedidos(request, id_pedido):
    pedidos = Pedidos.objects.get(id_pedido = id_pedido)

    return render(request,"editarPedidos.html",{"mispedidos":pedidos})


def editarPedidos(request):
    id_pedido = request.POST["txtidpedido"]
    nombre_pedido = request.POST["txtnombrepedido"]
    fecha = request.POST["txtfecha"]
    hora = request.POST["txthora"]
    id_producto = request.POST["txtidproducto"]
    id_cliente = request.POST["txtidcliente"]
    id_trabajador = request.POST["txtidtrabajador"]
    cantidad = request.POST["txtcantidad"]
    registro = request.POST["txtregistro"]

    pedido = Pedidos.objects.get(id_pedido = id_pedido)
    pedido.nombre_pedido = nombre_pedido
    pedido.fecha = fecha
    pedido.hora = hora
    pedido.id_producto = id_producto
    pedido.id_cliente = id_cliente
    pedido.id_trabajador = id_trabajador
    pedido.cantidad = cantidad
    pedido.registro = registro

    pedido.save()

    return redirect("pedidos")


def borrarPedidos(request, id_pedido):
    pedido = Pedidos.objects.get(id_pedido = id_pedido)
    pedido.delete()

    return redirect("pedidos")