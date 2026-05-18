from django.contrib import admin
from .models import Material, Orden, Existencia, Seccion, Categoria, Producto, Venta, DetalleVenta, Configuracion

admin.site.register(Material)
admin.site.register(Orden)
admin.site.register(Existencia)
admin.site.register(Seccion)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
admin.site.register(Configuracion)
