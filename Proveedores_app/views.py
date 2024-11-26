from django.shortcuts import render,redirect
from .models import Proveedores

# Create your views here.

def inicio_vistaProveedores(request):
    losproveedores = Proveedores.objects.all()

    return render(request,"gestionarProveedor.html",{"misproveedores":losproveedores})



def registrarProveedor(request):
    id_proveedor = request.POST["txtidproveedor"]
    nombre_empresa = request.POST["txtnombreempresa"]
    horarios = request.POST["txthorarios"]
    email = request.POST["txtemail"]
    celular = request.POST["txtcelular"]
    tipo = request.POST["txttipo"]
    direccion = request.POST["txtdireccion"]
    codigo_postal = request.POST["txtcodigopostal"]

    guardarproveedor = Proveedores.objects.create(id_proveedor=id_proveedor, nombre_empresa=nombre_empresa, horarios=horarios,
                                              email=email, celular=celular, tipo=tipo, direccion=direccion, codigo_postal=codigo_postal)

    return redirect("proveedores")

def seleccionarProveedor(request, id_proveedor):
    proveedores = Proveedores.objects.get(id_proveedor = id_proveedor)

    return render(request,"editarProveedor.html",{"misproveedores":proveedores})


def editarProveedor(request):
    id_proveedor = request.POST["txtidproveedor"]
    nombre_empresa = request.POST["txtnombreempresa"]
    horarios = request.POST["txthorarios"]
    email = request.POST["txtemail"]
    celular = request.POST["txtcelular"]
    tipo = request.POST["txttipo"]
    direccion = request.POST["txtdireccion"]
    codigo_postal = request.POST["txtcodigopostal"]

    proovedor = Proveedores.objects.get(id_proveedor = id_proveedor)
    proovedor.nombre_empresa = nombre_empresa
    proovedor.horarios = horarios
    proovedor.email = email
    proovedor.celular = celular
    proovedor.tipo = tipo
    proovedor.direccion = direccion
    proovedor.codigo_postal = codigo_postal

    proovedor.save()

    return redirect("proveedores")


def borrarProveedor(request, id_proveedor):
    trabajador = Proveedores.objects.get(id_proveedor = id_proveedor)
    trabajador.delete()

    return redirect("proveedores")