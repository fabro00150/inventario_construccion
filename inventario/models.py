from django.db import models

class Seccion(models.Model):
    nombre = models.CharField(max_length=100) # Ej: Arreglos Florales, Ropa, Cosmeticos, Juguetes
    descripcion = models.TextField(blank=True, null=True)

    def __get_total_productos(self):
        return self.productos.count()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name='categorias', null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.seccion.nombre} - {self.nombre}"

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    unidad_medida = models.CharField(max_length=50)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='materiales/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    seccion = models.ForeignKey(Seccion, on_delete=models.SET_NULL, null=True, related_name='productos')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='productos')
    foto = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    METODOS_PAGO = [
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia'),
    ]
    cliente_nombre = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente_nombre}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Configuracion(models.Model):
    nombre_sitio = models.CharField(max_length=100, default="Palo de Rosa")
    color_primario = models.CharField(max_length=7, default="#FFC0CB")
    color_secundario = models.CharField(max_length=7, default="#DB7093")
    whatsapp = models.CharField(max_length=20, default="573000000000")

    def __str__(self):
        return "Configuración del Sitio"

class Orden(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_orden = models.DateField(auto_now_add=True)

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
