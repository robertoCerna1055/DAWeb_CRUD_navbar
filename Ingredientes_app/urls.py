from django.urls import path
from Ingredientes_app import views 

urlpatterns = [
    path("ingredientes",views.inicio_vistaIngredientes,name="ingredientes"),
    path("registrarIngredientes/",views.registrarIngredientes,name="registrarIngredientes"),
    path("seleccionarIngredientes/<id_ingrediente>",views.seleccionarIngredientes,name="seleccionarIngredientes"),
    path("editarIngredientes/",views.editarIngredientes,name="editarIngredientes"),
    path("borrarIngredientes/<id_ingrediente>",views.borrarIngredientes,name="borrarIngredientes"),
]