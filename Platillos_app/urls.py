from django.urls import path
from Platillos_app import views 

urlpatterns = [
    path("platillos",views.inicio_vistaPlatillos,name="platillos"),
    path("registrarPlatillo/",views.registrarPlatillo,name="registrarPlatillo"),
    path("seleccionarPlatillo/<id_platillo>",views.seleccionarPlatillo,name="seleccionarPlatillo"),
    path("editarPlatillo/",views.editarPlatillo,name="editarPlatillo"),
    path("borrarPlatillo/<id_platillo>",views.borrarPlatillo,name="borrarPlatillo"),
]