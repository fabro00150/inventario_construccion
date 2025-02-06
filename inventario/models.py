from django.db import models

# Create your models here.

class Suministrador(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    unidad_medida = models.CharField(max_length=50)  # Ej: kg, litros, metros
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    suministrador = models.ForeignKey(Suministrador, on_delete=models.SET_NULL, null=True)
    foto = models.ImageField()
    
    def __str__(self):
        return self.nombre

class Orden(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_orden = models.DateField(auto_now_add=True)
    suministrador = models.ForeignKey(Suministrador, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        existencia, created = Existencia.objects.get_or_create(material=self.material)
        existencia.cantidad_disponible += self.cantidad
        existencia.save()

class Existencia(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    cantidad_disponible = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.material.nombre} - {self.cantidad_disponible} {self.material.unidad_medida}"