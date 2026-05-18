from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('catalogo/', views.catalogo, name='catalogo'),

    # Secciones
    path('secciones/', views.lista_secciones, name='lista_secciones'),
    path('secciones/agregar/', views.formulario_seccion, name='formulario_seccion'),
    path('secciones/editar/<int:id>/', views.formulario_seccion, name='editar_seccion'),
    path('secciones/eliminar/<int:id>/', views.eliminar_seccion, name='eliminar_seccion'),

    # Categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/agregar/', views.formulario_categoria, name='formulario_categoria'),
    path('categorias/editar/<int:id>/', views.formulario_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),

    # Materiales
    path('materiales/', views.lista_materiales, name='lista_materiales'),
    path('materiales/agregar/', views.formulario_material, name='formulario_material'),
    path('materiales/editar/<int:id>/', views.formulario_material, name='editar_material'),
    path('materiales/eliminar/<int:id>/', views.eliminar_material, name='eliminar_material'),

    # Productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/agregar/', views.formulario_producto, name='formulario_producto'),
    path('productos/editar/<int:id>/', views.formulario_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    # Ventas
    path('ventas/', views.lista_ventas, name='lista_ventas'),
    path('ventas/registrar/', views.registrar_venta, name='registrar_venta'),
    path('ventas/<int:id>/', views.detalle_venta, name='detalle_venta'),

    # Órdenes
    path('ordenes/', views.lista_ordenes, name='lista_ordenes'),
    path('ordenes/agregar/', views.formulario_orden, name='formulario_orden'),
    path('ordenes/editar/<int:id>/', views.formulario_orden, name='editar_orden'),
    path('ordenes/eliminar/<int:id>/', views.eliminar_orden, name='eliminar_orden'),

    # Existencias
    path('existencias/', views.lista_existencias, name='lista_existencias'),    
    path('existencias/eliminar/<int:id>/', views.eliminar_existencia, name='eliminar_existencia'),

    # Configuración
    path('configuracion/', views.configurar_sitio, name='configurar_sitio'),
]
