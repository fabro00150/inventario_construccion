from django.urls import path
from . import views

urlpatterns = [
    # Materiales
    path('', views.lista_materiales, name='lista_materiales'),
    path('materiales/agregar/', views.formulario_material, name='formulario_material'),
    path('materiales/editar/<int:id>/', views.formulario_material, name='editar_material'),
    path('materiales/eliminar/<int:id>/', views.eliminar_material, name='eliminar_material'),

    # Suministradores
    path('suministradores/', views.lista_suministradores, name='lista_suministradores'),
    path('suministradores/agregar/', views.formulario_suministrador, name='formulario_suministrador'),
    path('suministradores/formulario/', views.formulario_suministrador, name='formulario_suministrador'),
    path('suministradores/formulario/<int:id>/', views.formulario_suministrador, name='formulario_suministrador'),
    path('suministradores/<int:id>/', views.eliminar_suministrador, name='eliminar_suministrador'),

    # Órdenes
    path('ordenes/', views.lista_ordenes, name='lista_ordenes'),
    path('ordenes/agregar/', views.formulario_orden, name='formulario_orden'),
    path('ordenes/editar/<int:id>/', views.formulario_orden, name='formulario_orden'),
    path('ordenes/eliminar/<int:id>/', views.eliminar_orden, name='eliminar_orden'),

    # Existencias
    path('existencias/', views.lista_existencias, name='lista_existencias'),    
    path('existencias/eliminar/<int:id>/', views.eliminar_existencia, name='eliminar_existencia'),
]