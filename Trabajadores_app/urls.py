from django.urls import path
from Trabajadores_app import views 

urlpatterns = [
    path('trabajadores', views.inicio_vistaTrabajadores, name='trabajadores'),
    path('registrarTrabajador/', views.registrarTrabajador, name='registrarTrabajador'),
    path('seleccionarTrabajador/<id_trabajador>/', views.seleccionarTrabajador, name='seleccionarTrabajador'),
    path('editarTrabajador/', views.editarTrabajador, name='editarTrabajador'),
    path('borrarTrabajador/<id_trabajador>/', views.borrarTrabajador, name='borrarTrabajador'),
]
