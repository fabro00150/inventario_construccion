from django.contrib import admin

# Register your models here.
from .models import Suministrador, Material, Orden, Existencia

admin.site.register(Suministrador)
admin.site.register(Material)
admin.site.register(Orden)
admin.site.register(Existencia)