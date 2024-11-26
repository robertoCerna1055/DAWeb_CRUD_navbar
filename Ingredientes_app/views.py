from django.shortcuts import render,redirect
from .models import Ingredientes

# Create your views here.

def inicio_vistaIngredientes(request):
    losingredientes = Ingredientes.objects.all()

    return render(request,"gestionarIngredientes.html",{"misingredientes":losingredientes})



def registrarIngredientes(request):
    id_ingrediente = request.POST["txtidingrediente"]
    nombre_ingrediente = request.POST["txtnombreingrediente"]
    caducidad = request.POST["txtcaducidad"]
    codigo = request.POST["txtcodigo"]
    tipo = request.POST["txttipo"]
    descripcion = request.POST["txtdescripcion"]
    cantidad = request.POST["txtcantidad"]
    id_sucursal = request.POST["txtid_sucursal"]

    guardarsucursal = Ingredientes.objects.create(id_ingrediente=id_ingrediente, nombre_ingrediente=nombre_ingrediente, caducidad=caducidad,
                                              codigo=codigo, tipo=tipo, descripcion=descripcion, cantidad=cantidad, id_sucursal=id_sucursal)

    return redirect("ingredientes")

def seleccionarIngredientes(request, id_ingrediente):
    ingredientes = Ingredientes.objects.get(id_ingrediente = id_ingrediente)

    return render(request,"editarIngredientes.html",{"misingredientes":ingredientes})


def editarIngredientes(request):
    id_ingrediente = request.POST["txtidingrediente"]
    nombre_ingrediente = request.POST["txtnombreingrediente"]
    caducidad = request.POST["txtcaducidad"]
    codigo = request.POST["txtcodigo"]
    tipo = request.POST["txttipo"]
    descripcion = request.POST["txtdescripcion"]
    cantidad = request.POST["txtcantidad"]
    id_sucursal = request.POST["txtid_sucursal"]

    ingrediente = Ingredientes.objects.get(id_ingrediente = id_ingrediente)
    ingrediente.nombre_ingrediente = nombre_ingrediente
    ingrediente.caducidad = caducidad
    ingrediente.codigo = codigo
    ingrediente.tipo = tipo
    ingrediente.descripcion = descripcion
    ingrediente.cantidad = cantidad
    ingrediente.id_sucursal = id_sucursal

    ingrediente.save()

    return redirect("ingredientes")


def borrarIngredientes(request, id_ingrediente):
    ingrediente = Ingredientes.objects.get(id_ingrediente = id_ingrediente)
    ingrediente.delete()

    return redirect("ingredientes")